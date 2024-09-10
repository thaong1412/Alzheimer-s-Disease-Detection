# Alzheimer's Disease Detection Through Handwriting Analysis

## Project Overview

This project focuses on developing advanced machine learning models for the early detection of Alzheimer's disease using handwriting analysis. Utilizing the **DARWIN dataset**, collected from 174 participants (89 Alzheimer's patients and 85 healthy controls), we aim to improve predictive accuracy by analyzing detailed handwriting metrics recorded through a Wacom Bamboo tablet. The dataset contains **450 numerical features**, representing various handwriting characteristics across 25 distinct tasks.

### Key Features in the Dataset

The dataset captures various aspects of handwriting movements:
- **Time Features**:
  - Total Time (TT): Overall task duration
  - Air Time (AT): Time spent with the pen in the air
  - Paper Time (PT): Time spent writing on the paper
- **Speed Features**:
  - Mean Speed on-paper (MSP): Average speed of writing on paper
  - Mean Speed in-air (MSA): Average speed of pen movement in the air
- **Movement Smoothness Features**:
  - Mean Acceleration on-paper (MAP): Average acceleration of writing on paper
  - Mean Acceleration in-air (MAA): Average acceleration of pen movement in the air
  - Mean Jerk on-paper (MJP): Average jerk (change in acceleration) of writing on paper
  - Mean Jerk in-air (MJA): Average jerk of pen movement in the air
- **Pressure Features**:
  - Pressure Mean (PM): Average pressure exerted by the pen on the paper
  - Pressure Var (PV): Variance (fluctuation) of the pressure exerted by the pen
- **Global Mean Relative Tremor (GMRT) Features**:
  - GMRT on-paper (GMRTP): Measure of tremor during writing on paper
  - GMRT in-air (GMRTA): Measure of tremor during in-air movements
  - Mean GMRT (GMRT): Average of GMRTP and GMRTA
- **Other Features**:
  - Pendowns Number (PWN): Number of times the pen touches the paper
  - Max X Extension (XE): Maximum horizontal distance covered by writing
  - Max Y Extension (YE): Maximum vertical distance covered by writing
  - Dispersion Index (DI): Measure of how much of the paper is used for writing

### Objectives

1. **Enhance Predictive Accuracy for Alzheimer's Disease**: Develop and evaluate models to classify handwriting data from Alzheimer's patients and healthy controls, focusing on maximizing recall for high sensitivity.
   
2. **Optimize Feature Selection**: Apply various feature selection techniques to reduce the dimensionality of the dataset, preserving the most informative features while minimizing redundancy and multicollinearity.

3. **Evaluate Classifier Performance**: Compare the performance of multiple classifiers and ensemble methods to find the best-performing model.

4. **Implement Cross-Validation**: Use cross-validation to ensure models' robustness and generalizability to unseen data.

5. **Utilize Ensemble Learning**: Leverage ensemble techniques to combine the strengths of different classifiers for improved performance and stability.

### Bibliography

- Abdollahi, J., & Nouri-Moghaddam, B. (2022). A hybrid method for heart disease diagnosis utilizing feature selection-based ensemble classifier model generation. *Iranian Journal of Computer Science*, 5(3), 229–246. https://doi.org/10.1007/s42044-022-00104-x

- Mujahid, M., Rehman, A., Alam, T., Alamri, F. S., Fati, S. M., & Saba, T. (2023). An efficient ensemble approach for Alzheimer’s disease detection using an adaptive synthetic technique and deep learning. *Diagnostics*, 13(2489). Retrieved from https://www.sciencedirect.com/science/article/pii/S235291482100143X

- Öcal, H. (2023). A novel approach to detection of Alzheimer’s disease from handwriting: Triple ensemble learning model. *Journal of Applied Artificial Intelligence*. Retrieved from https://dergipark.org.tr/tr/download/article-file/3518417

- Shorewala, V. (2021). Early detection of coronary heart disease using ensemble techniques. *Informatics in Medicine Unlocked*, 26, 100655. https://doi.org/10.1016/j.imu.2021.100655

- Cilia, N. D., De Stefano, C., Fontanella, F., & Di Freca, A. S. (2018). An experimental protocol to support cognitive impairment diagnosis by using handwriting analysis. *Procedia Computer Science*, 141, 466–471. https://doi.org/10.1016/j.procs.2018.10.141

- Cilia, N. D., De Gregorio, G., De Stefano, C., Fontanella, F., Marcelli, A., & Parziale, A. (2022). Diagnosing Alzheimer’s disease from online handwriting: A novel dataset and performance benchmarking. *Engineering Applications of Artificial Intelligence*, 111, 104822. https://doi.org/10.1016/j.engappai.2022.10
