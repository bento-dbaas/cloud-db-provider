run:
	uvicorn cloud_db_provider.main:app --host 0.0.0.0 --port 80

deploy_dev:
	tsuru app deploy -a cloud-db-provider-dev .

deploy_prod:
	tsuru app deploy -a cloud-db-provider .

