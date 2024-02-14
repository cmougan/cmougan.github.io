black:
	python -m black .

gitall:
	git add .
	@read -p "Enter commit message: " message; 	git commit -m "$$message"
	git push



export_requirements:
	conda list --export > requirements.txt

install_requirements:
	conda install --file requirements.txt

notebook_memory_usage:
	conda install -c conda-forge jupyter-resource-usage


install_some_packages:
	conda install pip
	pip install jedi==0.17.2

run_script:
	jupyter nbconvert --to script ExploratoryDataAnalysis.ipynb
	python ExploratoryDataAnalysis.py

deploy:
	bundle exec jekyll liveserve

killport:
	kill -9 $(lsof -i:35729 -t)



