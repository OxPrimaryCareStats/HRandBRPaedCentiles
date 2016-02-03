HRandBRPaedCentiles
===================

Data and code relating to Fleming et al, Lancet 2011; 377(9770): 1011-8, doi:10.1016/S0140-6736(10)62226-X

**Downloading files**
You can download the whole set of files [here](https://github.com/susannahf/HRandBRPaedCentiles/archive/master.zip), or by clicking on the "Download ZIP" button.

The most commonly requested file is the [excel file of centile data](https://github.com/susannahf/HRandBRPaedCentiles/raw/master/HRandBRcentiles_rawdata_SD.xls).

You can download other individual files by clicking on the file name, and then clicking the "RAW" button.

*Use and attribution*
The data and code in this repository is made available under the GPLv3 license.  You are free to use, modify, and share these materials.  We ask that you reference the published paper (above) if you use the materials in a publication or publicly available material.

If you find this material particularly useful, we'd love to hear about it!  

*Included files:*

**DATA**

*kernelagecorrection.mat*    
Matlab data file.  
Contains two vectors: BRxhat and HRxhat, which are ages in years.
These act as indices to the contents of the structures BRmhat and HRmhat, which contain the centile data.
Obviously (hopefully), BRxhat and BRmhat are breathing rate data, and HRxhat and HRmhat are heart rate data.
The structures have the same contents - Mean (equiv to median as the data is symmetrical), Sigma (standard deviation), and various centiles.  Centile2_5 and Centile97_5 are the 2.5th and 97.5th centiles respectively.

*HRandBRcentiles_rawdata_SD.xls*    
Interpolated data at one month intervals for relevant centiles, mean and SD.
Data is also extracted at 1 day intervals up to 2 months for heart rate to capture the detail of the curve in infants.
This has been verified against the data in kernelagecorrection for fidelity of curves.

    
**MATLAB CODE** (commented)

*centilesforexcel.m*    
m file to interpolate data from kernelagecorrection to the format used in the included excel file

*kernelregression.m*    
general code for kernel regression, including variable bandwidth weighted kernel regression as used in the meta analysis


**WEB APPLICATION** (in subfolder)

Standalone html and js code to run web app for calculation of centiles at arbitrary age.
Does not need web access to run.
