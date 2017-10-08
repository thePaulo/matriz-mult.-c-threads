# matriz-mult.-c-threads
project that makes matrix multiplications

### Implementation
* project was made with c++ and multiplies the matrix that are on the files to be inputted with names like A4x4.txt and etc...
* execution may work with or without threads, depending on the execution input that is submitted

### Compiling 

* users shall use 
```
g++ -std=c++11 -pthread num.cpp -o exe
```

### Executing

* users shall use ./exe (size of the matrix) (OPTIONAL: num. of threads) 
ex: ```./exe 512 64 ``` multiplies a 512 by 512 matrix with 64 threads

* 1 parameter = no threads, 2 = with threads


