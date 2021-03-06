#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import pytest

from psychopy.visual.window import Window
from psychopy.visual.slider import Slider


class Test_Slider(object):
    def setup_class(self):
        self.win = Window([128,128], pos=[50,50], allowGUI=False,
                          autoLog=False)

    def teardown_class(self):
        self.win.close()

    def test_color(self):
        colors = ['black', 'red']

        for color in colors:
            s = Slider(self.win, color=color)

            assert s.line.color == color
            assert s.tickLines.colors == color

            for l in s.labelObjs:
                assert l.color == color

    def test_change_color(self):
        s = Slider(self.win, color='black')

        with pytest.raises(AttributeError):
            s.color = 'blue'

    def test_size(self):
        sizes = [(1, 0.1), (1.5, 0.5)]

        for size in sizes:
            s = Slider(self.win, size=size)
            assert s.size == size

    def test_change_size(self):
        s = Slider(self.win, size=(1, 0.1))

        with pytest.raises(AttributeError):
            s.size = (1.5, 0.5)

    def test_marker_scaling_factor(self):
        markerScalingFactors = [1, 1.0]

        for thisScalingFactor in markerScalingFactors:
            s = Slider(self.win, markerScalingFactor=thisScalingFactor)
            assert s.markerScalingFactor == thisScalingFactor

    def test_change_marker_scaling_factor(self):
        s = Slider(self.win, markerScalingFactor=1.0)

        with pytest.raises(AttributeError):
            s.markerScalingFactor = 0.5
