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

import pinutils;
info = {
 'name' : "Waveshare Port407Z",
 'link' :  [ "http://www.wvshare.com/product/Port407Z.htm" ],
 'default_console' : "EV_SERIAL2",
 'variables' : 2800,
 'binary_name' : 'espruino_%v_port407z.bin',
};
chip = {
  'part' : "STM32F407ZE",
  'family' : "STM32F4",
  'package' : "LQFP144",
  'ram' : 192,
  'flash' : 512,
  'speed' : 168,
  'usart' : 6,
  'spi' : 3,
  'i2c' : 3,
  'adc' : 3,
  'dac' : 2,
};
# left-right, or top-bottom order
board = {
  'top' : [ 'A1','3V3','VREFN','C3','C1','NRST','H0','F9','F7',
            '3V3','F5','F3','F1','C15','C13','E6','E4','E2' ],
  'top2' : [ 'A2', 'A0','VREFP','VDD','C2','C0','H1','F10','F8',
             'F6','GND','F4','F2','F0','C14','VBAT','E5','E3'],
  'left' : [ 'GND','A4','A6', 'C4', 'B0','B2','F12','3V3','F14',
             'G0','E7','E9','3V3','E11','E13','E15','B11','3V3'],
  'left2' : [ 'A3','3V3', 'A5', 'A7', 'C5','B1','F11','GND','F13',
              'F15','G1','E8','GND','E10','E12','E14','B10','NC'],
  'right2' : [ 'GND','E0','B8','B7','B5','B3','3V3','G14','G12','G10',
               'D7','3V3','D5','D3','D1','C12','C10','A14'],
  'right' : [ '3V3','E1','B9','BOOT0','B6','B4','G15','GND','G13',
              'G11','G9','D6','GND','D4','D2','D0','C11','A15'],
  'bottom' : [ 'B13','B15','D9','D11','D13','3V3','D15','G3','G5',
                'G7','GND','C6','C8','A8','A10','A12','NC','3V3'],
  'bottom2' : [ 'B12','B14','D8','D10','D12','GND','D14','G2','G4',
                'G6','G8','3V3','C7','C9','A9','A11','A13','GND'],
};
devices = {
  'OSC' : { 'pin_1' : 'H0',
            'pin_2' : 'H1' },
  'OSC_RTC' : { 'pin_1' : 'C14',
                'pin_2' : 'C15' },
  'LED1' : { 'pin' : 'A4' },
  'LED2' : { 'pin' : 'A5' },
  'LED3' : { 'pin' : 'A6' },
  'LED4' : { 'pin' : 'A7' },
  'BTN1' : { 'pin' : 'F13' },
  'BTN2' : { 'pin' : 'F14' },
  'BTN3' : { 'pin' : 'F15' },
  'USB' : { 'pin_otg_pwr' : 'A3',
            'pin_dm' : 'A11',
            'pin_dp' : 'A12',
          'pin_vbus' : 'A9',
            'pin_id' : 'A10', }
};


board_css = """
#board {
  width: 1100px;
  height: 2820px;
  left: 200px;
  top: 200px;
  background-image: url(img/PORT407Z.jpg);
}
#boardcontainer {
  height: 3500px;
}
#top {
  top: 10px;
  right: 340px;
}
#top2 {
  top: 100px;
  right: 340px;
}
#left {
  top: 1580px;
  right: 900px;
}
#left2 {
  top: 1580px;
  left: 260px;
}
#right  {
  top: 880px;
  left: 850px;
}
#right2  {
  top: 880px;
  right: 300px;
}
#bottom {
  top: 2790px;
  right: 340px;
}
#bottom2 {
  top: 2700px;
  right: 340px;
}
""";

def get_pins():
  pins = pinutils.scan_pin_file([], 'stm32f40x.csv', 6, 9, 10)
  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])
