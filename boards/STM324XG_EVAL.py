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
 'name' : "ST STM324XG-EVAL",
 'link' :  [ "http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1199/PF252217?s_searchtype=partnumber" ],
 'default_console' : "EV_SERIAL2",
 'variables' : 5450,
 'binary_name' : 'espruino_%v_stm324xg_eval.bin',
};
chip = {
  'part' : "STM32F417IG",
  'family' : "STM32F4",
  'package' : "UFBGA176",
  'ram' : 192,
  'flash' : 1024,
  'speed' : 168,
  'usart' : 6,
  'spi' : 3,
  'i2c' : 3,
  'adc' : 3,
  'dac' : 2,
};
# bottom: CN1, even ascending
# bottom2: CN1, odd ascending
# right: CN2, odd descending
# right2: CN2, even descending
# top: CN3, even ascending
# top2: CN3, odd ascending
# left: CN4, even descending
# left2: CN4, odd descending

board = {
  'bottom2' : [ 'E2','E4','E6','C13','GND','I9','I11','F1','F3',
            'F4','F6','F8','F10','H1','GND','C2','VREF+','A1',
            'H2','H3','H5','NC','NC','3V3','GND' ],
  'bottom' : [ 'GND','E3','E5','I8','C14','C15','I10','F0','F2',
             'GND','F5','F7','F9','H0','C0','C1','C3','A0',
             'A2','GND','H4','NC','NC','3V3','5V' ],

  'right2' : [ 'GND','H9','H7','B11','E15','E14','E12','E10','E8',
              'G1','GND','F14','F12','B2','B0','C5','A7','A5',
              'A3','GND' ],

  'right' : [ 'H11','H10','H8','H6','B10','GND','E13','E11','E9',
               'E7','G0','F15','F13','F11','B1','GND','C4','A6',
               'A4','VCC' ],

  'top2' : [ 'GND','I1','H15','H13','C13','NRST','A11','A9','C9',
               'EMU_5V','C6','G7','G5','G3','D15','D14','D12','D10',
               'D8','GND','B13','H12','NC','EMU_3V3','EMU_5V' ],

  'top' : [ 'I2','I0','H14','A13','GND','A12','A10','A8','C8',
            'C7','G8','G6','G4','G2','GND','D13','D11','D9',
            'B15','B14','B12','NC','NC','APP_3V3','GND' ],

  'left2' : [ 'GND','A15','C11','D0','D2','D3','D5','D7','G10',
              'G12','GND','G15','B4','B6','BOOT0','B8','E0','I4',
              'I6','GND' ],

  'left' : [ 'I3','A14','C10','C12','D1','GND','D4','D6','G9',
             'G11','G13','G14','B3','B5','B7','GND','B9','E1',
             'I5','I7' ],
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
  'BTN1' : { 'pin' : 'A0' },
  'BTN2' : { 'pin' : 'C13' },
  'BTN3' : { 'pin' : 'G15' },
  'USB' : { 'pin_otg_pwr' : 'H5',
            'pin_dm' : 'A11',
            'pin_dp' : 'A12',
          'pin_vbus' : 'A9',
            'pin_id' : 'A10', },
  'SD' :  { 'pin_cmd' :  'D2',
            'pin_cd' :  'H13',
            'pin_d0' :  'C8',
            'pin_d1' :  'C9',
            'pin_d2' :  'C10',
            'pin_d3' :  'C11',
            'pin_clk' :  'C12' },
  'LCD' : {
            'width' : 320, 'height' : 240, 'bpp' : 16, 'controller' : 'fsmc',
            'pin_d0' : 'D14',
            'pin_d1' : 'D15',
            'pin_d2' : 'D0',
            'pin_d3' : 'D1',
            'pin_d4' : 'E7',
            'pin_d5' : 'E8',
            'pin_d6' : 'E9',
            'pin_d7' : 'E10',
            'pin_d8' : 'E11',
            'pin_d9' : 'E12',
            'pin_d10' : 'E13',
            'pin_d11' : 'E14',
            'pin_d12' : 'E15',
            'pin_d13' : 'D8',
            'pin_d14' : 'D9',
            'pin_d15' : 'D10',
            'pin_rd' : 'D4',    # NOE
            'pin_wr' : 'D5',    # NWE
            'pin_cs' : 'G10',   # NE3
            'pin_rs' : 'F0'    # A0
          },
  'JTAG' : {
        'pin_MS' : 'A13',
        'pin_CK' : 'A14', 
        'pin_DI' : 'A15' 
          }
};


board_css = """
#board {
  width: 1325px;
  height: 3525px;
  left: 200px;
  top: 200px;
  background-image: url(img/STM3241G_EVAL.jpg);
}
#boardcontainer {
  height: 5000px;
}
#top {
  top: 190px;
  right: 340px;
}
#top2 {
  top: 270px;
  right: 340px;
}
#left {
  top: 2130px;
  right: 980px;
}
#left2 {
  top: 2130px;
  left: 384px;
}
#right  {
  top: 2130px;
  right: 350px;
}
#right2  {
  top: 2130px;
  right: 300px;
}
#bottom {
  top: 980px;
  right: 340px;
}
#bottom2 {
  top: 890px;
  right: 340px;
}
""";

def get_pins():
  pins = pinutils.scan_pin_file([], 'stm32f40x.csv', 6, 9, 10)
  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])
