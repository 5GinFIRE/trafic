#!/bin/bash

set -eu

LABEL=${LABEL:-"lola-flows"}
CONF=${CONF:-flows.env}
DB=${DB:-lola}

base=$(dirname $0)
. ${base}/${CONF}

schedule clients \
	--log-tag=C \
	--flows-dirs=${FLOWS} \
	--influxdb-enabled \
	--influxdb-endpoint=http://influxdb:8086 \
	--influxdb-db=lola-${DB} \
	--influxdb-measurements=${LABEL}
