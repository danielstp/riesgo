#!/bin/bash -x

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

MODELOS=`find $DIR/.. -name models.py | xargs grep -E "class " | grep -v Meta | sed "s|^$DIR/../riesgo_ductos/\([a-zA-Z0-9]\+\)/models.py:class \([a-zA-Z0-9]\+\)([0-9a-zA-Z\.]\+):|\1.\2|g"`

for modelo in $MODELOS
do
    app=$(echo $modelo | sed "s/^\([a-zA-Z0-9]\+\)\.\([a-zA-Z0-9]\+\)/\1/")
    mod=$(echo $modelo | sed "s/^\([a-zA-Z0-9]\+\)\.\([a-zA-Z0-9]\+\)/\2/")
    $DIR/../manage.py dumpdata $modelo > $DIR/../riesgo_ductos/fixtures/$modelo.json
done