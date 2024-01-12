# detect-object-classification-with-YOLOv8

## Tools

1. Python Language
2. Visual Studio Code [https://code.visualstudio.com/download]
3. Google Colaboratory [https://colab.research.google.com/]
4. Git [https://git-scm.com/downloads]
5. Github [https://github.com]
6. Terminal (Powershell, Iterm, Command Prompt (CMD), Bash, Zsh, Fish, etc)


## Dataset

If you want a dataset like mine, you can download it at the following link: '[Dataset](https://drive.google.com/file/d/1PDOOE_4dVe5W_jRhQZkKkFgDVyjp7xwl/view?usp=sharing)'.

## How to Train Data in Local

1. I assume you have Python language installed and a dataset on your device. The first step is that you have to install the library in the terminal by typing this command:

```bash
pip install ultralytic
```

2. If you already have the ultralytics library in your working folder. You can confirm the directory where the .yaml file is located.
3. Next, you have to adjust the contents of the .yaml file, such as the dataset directory and class label naming.
4. If you have completed steps one to three, run the train.py file or write the following command in the terminal:

```bash
python train_data.py
```


## How to Train Data in Google Colab

1. I assume you already have a dataset that matches the example. The first step is to upload the dataset file to Google Drive.
2. Next, upload the .yaml file and adjust the contents of the file in Google Drive.
3. Then, create a Google Colab file or copy the .ipnyb file to your drive.
4. If so, execute each command in the Google Colab file.

```bash
$ gcc main -o main.c && ./main
```

## How to Detect File Photo or Video
I assume you have finished training the data so you already have a YOLOv8 model.
If you want to detect photos or videos, adjust the contents of the file source directory and execute the following command in the terminal:

```bash
python predict_foto.py
```
```bash
python predict_video.py
```


The following is the project structure that must be used in local.

```bash
.
├── README.md
├── detectObjectClassificationWithYolov8
│   ├── Dataset
│   │   ├── Train
│   │   │   ├── images (.jpeg/.jpg/.png)
│   │   │   ├── label (.txt)
│   │   ├── Validasi
│   │   └── Test
│   ├── config.yaml
│   ├── train.py or train_data.ipnyb
│   ├── predict_foto.py
│   ├── predict_video.py
│   ├── Video or Photo or Data
│   ...
...
```
