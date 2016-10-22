mkdir -p msweb
cd msweb

wget -c "http://archive.ics.uci.edu/ml/machine-learning-databases/anonymous/anonymous-msweb.test"

wget -c "http://archive.ics.uci.edu/ml/machine-learning-databases/anonymous/anonymous-msweb.data"

wget -c "http://archive.ics.uci.edu/ml/machine-learning-databases/anonymous/anonymous-msweb.info"

cd ../


python generate-menu.py msweb/anonymous-msweb.data
