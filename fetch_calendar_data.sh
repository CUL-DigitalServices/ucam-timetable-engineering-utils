#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

mkdir -p $DIR/data/IA $DIR/data/IB $DIR/data/IIA $DIR/data/IIB

BASE_URL="http://td.eng.cam.ac.uk/tod/public/view_ical.php?yearval=2013_14"

curl "$BASE_URL&term=M&course=IA" > $DIR/data/IA/michaelmas.ics
curl "$BASE_URL&term=L&course=IA" > $DIR/data/IA/lent.ics
curl "$BASE_URL&term=E&course=IA" > $DIR/data/IA/easter.ics

curl "$BASE_URL&term=M&course=IB" > $DIR/data/IB/michaelmas.ics
curl "$BASE_URL&term=L&course=IB" > $DIR/data/IB/lent.ics
curl "$BASE_URL&term=E&course=IB" > $DIR/data/IB/easter.ics

curl "$BASE_URL&term=M&course=IIA" > $DIR/data/IIA/michaelmas.ics
curl "$BASE_URL&term=L&course=IIA" > $DIR/data/IIA/lent.ics
curl "$BASE_URL&term=E&course=IIA" > $DIR/data/IIA/easter.ics

curl "$BASE_URL&term=M&course=IIB" > $DIR/data/IIB/michaelmas.ics
curl "$BASE_URL&term=L&course=IIB" > $DIR/data/IIB/lent.ics
curl "$BASE_URL&term=E&course=IIB" > $DIR/data/IIB/easter.ics
