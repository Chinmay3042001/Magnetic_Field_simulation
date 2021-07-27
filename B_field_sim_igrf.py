import igrf
import pymap3d as fc

def magnetic_field_eci(time,latitude,longitude,altitude):
    magnetic_field_ned = igrf.igrf(time,latitude,longitude,altitude)
    magnetic_field_eci = fc.ecef2eci(fc.ned2ecef(magnetic_field_ned))

    return magnetic_field_eci


