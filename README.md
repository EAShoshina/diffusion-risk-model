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

