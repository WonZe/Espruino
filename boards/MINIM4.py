#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2014 Fran Taylor <narf@alum.mit.edu>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------
#
# to program:
# 
#            MINI-M4   ST-Link/V2 
# VDD          32         1
# GND          31         8
# RST           1        15
# SWCLK(A14)   35         9
# SWDIO(A13)   36         7

import pinutils;
info = {
 'name' : "Mikroe Mini-M4",
 'link' :  [ "http://www.mikroe.com/mini/stm32/" ],
 'default_console' : "EV_SERIAL2",
 'variables' : 5450,
 'binary_name' : 'espruino_%v_minim4.bin',
};
chip = {
  'part' : "STM32F415RGT6",
  'family' : "STM32F4",
  'package' : "LQFP64",
  'ram' : 192,
  'flash' : 1024,
  'speed' : 168,
  'usart' : 6,
  'spi' : 3,
  'i2c' : 3,
  'adc' : 3,
  'dac' : 2,
};
# left-right, or top-bottom order
board = {
  'left' : [ 'RST','A0','A1', 'A2', 'A3','C0','B12','C1','C2',
             'A8','3V3','GND','B9','B8','C9','B4','B5','B13','B0','B1'],
  'right' : [ 'A6','A7','A5','A4','A14','A13','C4','C5','3V3',
              'GND','A15','B3','B10','B11','B7','B6','B15','B14','C11','C10']
};
devices = {
  'OSC' : { 'pin_1' : 'H0',
            'pin_2' : 'H1' },
  'OSC_RTC' : { 'pin_1' : 'C14',
                'pin_2' : 'C15' },
  'LED1' : { 'pin' : 'C12' },
  'LED2' : { 'pin' : 'C13' },
  'USB' : { 'pin_dm' : 'A11',
            'pin_dp' : 'A12',
            'pin_vbus' : 'A9',
            'pin_id' : 'A10', }
};


board_css = """
#board {
  width: 475px;
  height: 750px;
  left: 150px;
  top: 0px;
  background-image: url(img/MIKROE-MINIM4.jpg);
}
#boardcontainer {
  height: 800px;
}
#left {
  top: 120px;
  right: 320px;
}
#right  {
  top: 120px;
  left: 320px;
}
""";

def get_pins():
  pins = pinutils.scan_pin_file([], 'stm32f40x.csv', 6, 9, 10)
  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])
