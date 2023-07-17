from calculate import execute
#test scripts for the execute function (to test the execution of the input statements)

#insert 5 test cases
#add test
def test_add():
    assert execute([1,2,3],"x + 2") == [3,4,5]
#subtract test
def test_subtract():
    assert execute([1,2,3],"x - 2") == [-1,0,1]
#mult test
def test_mult():
    assert execute([1,2,3],"x * 2") == [2,4,6]
#div test
def test_div():
    assert execute([1,2,3],"x / 2") == [0.5,1,1.5]
#power
def test_power():
    assert execute([1,2,3],"x ^ 2") == [1,4,9]

