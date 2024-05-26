import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, light

from esphome.const import (
    CONF_ID,
    CONF_OUTPUT_ID,
    CONF_LIGHT
)
from esphome.components.light import LightState

MULTI_CONF = True

AUTO_LOAD = [ "light" ]

DEPENDENCIES = ['i2c']

fourchdimmer_ns = cg.esphome_ns.namespace('fourchdimmer')
FourChDimmer = fourchdimmer_ns.class_('FourChDimmer', i2c.I@CDevice, cg.Component)

CONFIG_SCHEMA = light.BRIGHTNESS_ONLY_LIGHT_SCHEMA.extend(
    {
        cv.GenerateID(CONF_ID): cv.declare_id(LightState),
        cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(FourChDimmer)
    }
).extend(i2c.i2c_device_schema(0x20)

