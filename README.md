# Introduction 
We want to benchmark algorithms for private data synthesis, particularly for spatio-temporal data synthesis. This can have profund impact on multiple areas, especially in public health

### Usage 

### Running using Docker

Build the image

```docker build -t evaluation_container . ```

Run the container

```docker run -v dataset:/app/dataset/ -t -i dataset_eval ```

The dataset folder should contain your target dataset with the name "dataset.csv".

The script trains and evaluates TabNet, Random Forest and MLP on all possible combinations of categorical data.

### Contributors to the code/project (random order)
1. Mikhail Dmitrienko
2. Sheshank Shankar
3. Soham Dasgupta
4. Ishaan Singh
5. Rohan Sukumaran
6. Abhishek Singh
7. Praneeth Vepakomma
8. Hrishikesh Kamath
