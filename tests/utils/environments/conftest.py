#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fixtures for tests"""

# Import modules
import os
import pytest
import numpy as np
from mock import Mock
import matplotlib as mpl

if os.environ.get('DISPLAY','') == '':
    mpl.use('Agg')

# Import from package
from pyswarms.single import GlobalBestPSO
from pyswarms.utils.environments import PlotEnvironment
from pyswarms.utils.functions.single_obj import sphere_func

@pytest.fixture
def mock_pso():

    def _mock_pso(index):
        class_methods = [
            'get_cost_history',
            'get_pos_history',
            'get_velocity_history',
            'optimize',
            'reset'
        ]

        get_specs = lambda idx: [x for i,x in enumerate(class_methods) if i != idx]

        return Mock(spec=get_specs(index))

    return _mock_pso

@pytest.fixture
def plot_environment():
    optimizer = GlobalBestPSO(10, 3, options={'c1': 0.5, 'c2': 0.3, 'w': 0.9})
    return PlotEnvironment(optimizer, sphere_func, 1000)