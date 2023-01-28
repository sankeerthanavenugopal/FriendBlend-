# Friend Blend

## Brief Description

This project contains a program to combine images of two people taken at the same location with similar perspectives to obtain a single image that contains both people. It is achieved using python with the help of opencv.

Documentation of the project can be found [here](https://www.notion.so/Friend-Blend-Documentation-eb0e980be417494b87dfb75998c361b6).

Presentation for the final evals can be found [here](https://www.canva.com/design/DAFTP2PEPIU/NLc7W1nEgJseUAxFOcr0og/view?utm_content=DAFTP2PEPIU&utm_campaign=designshare&utm_medium=link&utm_source=publishpresent)
## Setup and Installation

### Preliminary setup

- Install python 3 (version $\geq$ 3.9) from [here](https://www.python.org/downloads/)

### Project setup

- Clone and enter into this repository with the command

```bash
git clone https://github.com/Digital-Image-Processing-IIITH/dip-m22-project-big-dipper-22.git
cd dip-m22-project-big-dipper-22
```

- Download the test images and outputs from [here](https://drive.google.com/file/d/1VtuDR5_bO7NlZZlJ8Kh7QL4N1K60q3lI/view?usp=share_link) and extract it to the `data` directory in the cloned repository

- Create and activate a python virtual environment inside the repository using

```bash
python -m venv .venv
./.venv/scripts/activate
```

- To download all the required python modules, run

```bash
pip install -r requirements.txt
```

- The project code is in the notebook `/src/full_new.ipynb`
- Replace the variable `image_num` with numbers `1-15` in the notebook to run any desired image.
- The output will be shown at the end of the notebook and is also exported to `data/outs/image_num.jpg`

## Sample outputs

### Successful

Inputs:

Image 1:
![Image 1](https://i.imgur.com/Fe4Ukgk.jpg)
Image 2:
![Image 2](https://i.imgur.com/acwiWZQ.jpg)

Output:
![Output](https://i.imgur.com/fLDQUhk.jpg)

### Unsuccessful

Inputs:
Image 1:
![Image 1](https://i.imgur.com/xOQcZg5.jpg)
Image 2:
![Image 2](https://i.imgur.com/2cavGqc.jpg)

Output:
![Output](https://i.imgur.com/JIQXXif.png)
Perspective warping fails in the above case since the background does not have enough texture.

## Team Information

Team name: Big Dipper
Team members:

- Maulesh Gandhi - 2020112009
- Sankeerthana Venugopal - 2020102008
- Sreenya Chitluri - 2020102065
- Tejah S S - 2020112028

## Biblography

- [1] [FriendBlend](https://web.stanford.edu/class/ee368/Project_Spring_1415/Reports/Chen_Zeng.pdf): The paper that we tried to replicate
- [2] [OpenCV Documentation](https://docs.opencv.org/): The library used for image processing
- [3] [Python](https://www.python.org/): The programming language used
- [4] [StackOverflow](https://stackoverflow.com/): The website that helped us with the code
