# Sentimental Analysis

Sentimental Analysis is a Python program made for Treehacks 2019 by Nick Chen, Elaine Nguyen, Jenna Lau, and Julia Cordero. The base libraries we use include Microsoft's Cognitive Face API for Azure, cv2, numpy, pandas, and Dash by Plotly.

For more information on Sentimental Analysis, visit our website at https://elainen1.wixsite.com/emotion

## Getting Started

### Prerequisites

Libraries and how to install them

Cognitive Face
* pip3 install cognitive_face
NOTE: need a subscription key through azure

OPENCV (cv2)
	pip3 install opencv-python (might need --user flag)

NUMPY
	pip3 install numpy

PANDAS
	pip3 install pandas

Dash by Plotly
	pip install dash==0.36.0  # The core dash backend
	pip install dash-html-components==0.13.5  # HTML components
	pip install dash-core-components==0.43.0  # Supercharged components
	pip install dash-table==3.1.11  # Interactive DataTable component (new!)
	pip install dash-daq==0.1.0  # DAQ components (newly open-sourced!)

## Before Deployment

* replace KEY with your own azure key, change os dir to the proper directory with os.chdir, and set the cv2 BASE_URL

## Deployment
1. Download, unzip, and open this repository. 
2. Follow the Before Deployment instructions above.
3. run 'python sentimental_analysis.py test' in the appropriate folder in the terminal

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
