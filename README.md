[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EAShoshina/diffusion-risk-model/blob/main/diffusion_model_training.ipynb)

# Diffusion Model for Financial Risk Estimation

Repository created within the framework of undergraduate thesis preparation.

## Functionality

- Loading financial data (S&P 500)
- Log-return computation
- Forward diffusion process
- Noise prediction neural network
- Synthetic trajectory generation
- VaR and Expected Shortfall calculation

## Structure
`diffusion_model_training.ipynb` – главный Jupyter ноутбук со всем кодом:
- Загрузка данных S&P 500
- Реализация диффузионной модели
- Нейронная сеть для предсказания шума
- Обучение модели
- Расчет риск-метрик (VaR, ES)
- Визуализация результатов



