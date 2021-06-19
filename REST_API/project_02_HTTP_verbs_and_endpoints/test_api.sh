curl http://127.0.0.1:5000/store
echo "test 01 ok"

curl http://127.0.0.1:5000/store/My%20store%20name
echo "test 02 ok"

curl http://127.0.0.1:5000/store/My%20store%20name/item
echo "test 03 ok"
