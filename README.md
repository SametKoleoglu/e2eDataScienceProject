
# Zoe Depth Estimation API

A brief description of what this project does and who it's for


## Usage/Examples

```bash
usage: cli.py [-h] input_image output_image

Depth Estimation CLI Using ZoeDepth

positional arguments:
  input_image   Path to the input image file
  output_image  Path to the output depth map

options:
  -h, --help    show this help message and exit

  
## API Usage
http://localhost:8001/docs
http://localhost:8001/predict

## Installation 

Install depth estimation project with pip

```bash 
  pip install -r requirements.txt
```
    
## Environment Variables

`IMG_API_KEY`

  
## Depoloyment

```bash
  docker build -t depth_estimation .
  docker run -d -p 8001:8001 depth_estimation
```

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  