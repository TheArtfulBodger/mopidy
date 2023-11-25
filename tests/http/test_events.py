import json
import unittest
from unittest import mock

from mopidy.http import actor


@mock.patch("mopidy.http.handlers.WebSocketHandler.broadcast")
class HttpEventsTest(unittest.TestCase):
    def setUp(self):
        self.io_loop = mock.Mock()

    def test_track_playback_paused_is_broadcasted(self, broadcast):
        actor.on_event_original("track_playback_paused", self.io_loop, foo="bar")

        self.assertDictEqual(
            json.loads(str(broadcast.call_args[0][0])),
            {"event": "track_playback_paused", "foo": "bar"},
        )

    def test_track_playback_resumed_is_broadcasted(self, broadcast):
        actor.on_event_original("track_playback_resumed", self.io_loop, foo="bar")

        self.assertDictEqual(
            json.loads(str(broadcast.call_args[0][0])),
            {"event": "track_playback_resumed", "foo": "bar"},
        )


@mock.patch("mopidy.http.handlers.WebSocketHandler.broadcast")
class HttpJsonRPCEventsTest(unittest.TestCase):
    def setUp(self):
        self.io_loop = mock.Mock()

    def test_track_playback_paused_is_broadcasted(self, broadcast):
        actor.on_event_jsonrpc("track_playback_paused", self.io_loop, foo="bar")

        self.assertDictEqual(
            json.loads(str(broadcast.call_args[0][0])),
            {
                "jsonrpc": "2.0",
                "method": "event.track_playback_paused",
                "params": {"foo": "bar"},
            },
        )

    def test_track_playback_resumed_is_broadcasted(self, broadcast):
        actor.on_event_jsonrpc("track_playback_resumed", self.io_loop, foo="bar")

        self.assertDictEqual(
            json.loads(str(broadcast.call_args[0][0])),
            {
                "jsonrpc": "2.0",
                "method": "track_playback_resumed",
                "params": {"foo": "bar"},
            },
        )
