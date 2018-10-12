# power_prop_test
Function to compute the power or other parameters of a two-samples test for proportions. Function writen in python.

![](http://latex.codecogs.com/gif.latex?p_o%20%3D%20%5Cfrac%7Bp_1n_1%20&plus;%20p_2n_2%7D%7Bn_1%20&plus;%20n_2%7D)
<br>
if:
<br>
![](http://latex.codecogs.com/gif.latex?n_1%20%3D%20n_2%20%3D%20n)
<br>
then:
![](http://latex.codecogs.com/gif.latex?p_o%20%3D%20%5Cfrac%7Bp_1%20&plus;%20p_2%7D%7B2%7D)
<br>
We have:
![](http://latex.codecogs.com/gif.latex?Z_c%20%3D%20p_1%20&plus;%20Z_%5Calpha%5Csqrt%7B%20p_o%281%20-%20p_o%29%20*%20%282/n%29%20%7D%20%3D%20p_1%20&plus;%20Z_%5Calpha%5Csqrt%7B%20%5Cfrac%7Bp_1%20&plus;%20p_2%7D%7B2%7D%281%20-%20%5Cfrac%7Bp_1%20&plus;%20p_2%7D%7B2%7D%20%29%20*%20%5Cfrac%7B2%7D%7Bn%7D%7D%20%281%29)
<br>
and
![](http://latex.codecogs.com/gif.latex?Z_c%20%3D%20p_2%20-%20Z_%5Cbeta%5Csqrt%7B%20%5Cfrac%7Bp_1%281%20-%20p_1%29%7D%7Bn%7D%20&plus;%20%5Cfrac%7Bp_2%281%20-%20p_2%29%7D%7Bn%7D%20%7D%20%3D%20p_2%20-%20Z_%5Cbeta%5Csqrt%7B%20%28%20p_1%281%20-%20p_1%29%20&plus;%20p_2%281%20-%20p_2%29%20%29%20%5Cfrac%7B1%7D%7Bn%7D%20%7D%20%282%29)