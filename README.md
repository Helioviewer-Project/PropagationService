# Solar System Propagation Service

Mock-up propagation RPC server.

Currently geared for radial propagation with fixed speed.

## Functions

- `propagate`
  - Arguments:
    - `name` (ignored) - quantity
    - `utc` - start of time range
    - `utc_end` (optional) - end of time range
    - `deltat` (optional) - time step
  - Returns: rectangular coordinates position of SOHO in HEEQ reference frame in km and fixed propagation speed of 1000km/s.

## Installation

A sample Dockerfile is provided, as well as a bootstrap script that assumes Python 3 in the `service` directory.
It connects to the SWHV GeometryService and runs on port 7790.
