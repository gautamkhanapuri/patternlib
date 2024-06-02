username="gautamkhanapuri"
cd code
export PYTHONPATH=`pwd`
cd ..
python3 -m venv patternenv
source patternenv/bin/activate
ver=`cat code/patternlib/__init__.py  |  grep 'VERSION =' | sed -e "s/VERSION = //" -e 's/"//g'`
pip install -U pip setuptools wheel
python3 setup.py bdist_wheel
docker build -t ${username}/patternlib:${ver} --build-arg APP_VERSION=${ver} .
docker run --rm --name pattern ${username}/patternlib:${ver}
deactivate 
/bin/rm -rf build dist patternenv code/patternlib.egg-info code/__pycache__
echo "To run again these patterns...."
echo "docker run --rm --name pattern ${username}/patternlib:${ver} --show hour_glass"
echo "To run other patterns....run interactively"
echo "docker run --rm --name pattern -it --entrypoint /bin/bash ${username}/patternlib:${ver}"
echo "At the prompt of #, run this command ...."
echo "python /root/eg.py --run e_pattern --param 5"
