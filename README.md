# Barcelona_Streetscape_Quality_Analysis
How Street-View Features Influencing Perceived Streetscape Quality: The Case of Barcelona

This project, developed at UCL CASA (Centre for Advanced Spatial Analysis), focuses on investigating how the visual perception of streetscapes influences people's impressions of different places. For a comprehensive overview of this research, please refer to the Program_Analysis.ipynb notebook.

All contents see the main file: `Program_Analysis.ipynb`

The program outlined in this notebook includes several detailed steps:
1. Downloading Street View Images: Utilizes the Google Earth API to retrieve street view images for analysis.
2. Image Semantic Segmentation: Implements advanced techniques to segment images into meaningful parts, enhancing the analysis of visual components.
3. Volunteer Grading Mini-Program: Engages volunteers to grade images, thereby collecting subjective data on streetscape quality.
4. Building a Random Forest Regression Model: Constructs a model to predict the perceived quality of views based on image features and volunteer ratings.
5. Exploring Spatial Analysis Techniques: Applies techniques such as Ordinary Least Squares (OLS) and Geographically Weighted Regression (GWR) to understand spatial variances in perception.

This program serves as an excellent introductory tutorial for those interested in applying street-view analysis in urban studies. Whether you're a student, researcher, or practitioner, this guide provides valuable insights and practical steps to leverage visual data for urban perception studies.

Due to space limits the segmentation model is removed in github, which need to be mannually downloaded from OneDrive https://liveuclac-my.sharepoint.com/:f:/r/personal/ucfnonb_ucl_ac_uk/Documents/Assignment_Final/image_download_segmentation/semantic_segmentation/ckpt/ade20k-resnet50dilated-ppm_deepsup?csf=1&web=1&e=b2tkG1  and put them under the right folder. All necessary files are also available on this OneDrive link, one could also download all directly to run the program.

Overall, this study got some interesting findings. Research indicates significant spatial variations in the impact of visual elements on perceived streetscape quality across different areas of Barcelona. this study proposes a new theoretical and methodological framework for streetscape research, emphasizing the spatial heterogeneity in the influence of visual elements and suggesting innovative approaches for urban renewal strategies. Future research should explore the impact mechanisms of various feature combinations on perceived quality. The study's limitations include limited training data, potentially heightening the influence of volunteer subjectivity. Future work should expand sample sizes and enhance predictive models to improve reliability. Moreover, the generalizability of these findings needs further validation, as influence patterns may differ across various urban and cultural contexts.


