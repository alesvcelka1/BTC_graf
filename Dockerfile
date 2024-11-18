# Použijte oficiální Python image jako základ
FROM python:3.9-slim

# Nastavte pracovní adresář v kontejneru
WORKDIR /app

# Zkopírujte requirements.txt do pracovního adresáře
COPY requirements.txt .

# Nainstalujte závislosti
RUN pip install --no-cache-dir -r requirements.txt

# Zkopírujte zbytek aplikace do pracovního adresáře
COPY . .

# Exponujte port, na kterém Flask běží
EXPOSE 5000

# Definujte příkaz pro spuštění aplikace
CMD ["python", "app.py"]