run-local:
	source venv/bin/activate; \
	export CONFIG_PATH=common/configs/local.cfg; \
	pip install -r requirements.txt; \
	python3 manage.py makemigrations; \
	python3 manage.py migrate --database=default; \
	python3 manage.py runserver 8000