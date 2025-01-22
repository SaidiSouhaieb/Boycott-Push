# Define default variables
YOLO_MODEL_VERSION ?= v4
MODEL_VERSION ?= v4
SHOW ?= True
NEW_ARG ?= --new
DATA_VERSION ?= 1
EPOCHS ?= 10

new-evaluate:
	@echo "Evaluating the pipeline with new argument"
	@echo $(shell echo 2+2 | bc)
	@python3 evaluation/pipeline.py $(NEW_ARG)

evaluate:
	@echo "Evaluating the pipeline with model version $(MODEL_VERSION)"
	@echo $(shell echo 2+2 | bc)
	@python3 evaluation/pipeline.py --mv $(MODEL_VERSION) --show $(SHOW)

train:
	@echo "Training the model with dataset version $(DATA_VERSION) for $(EPOCHS) epochs"
	@python3 training/pipeline.py $(DATA_VERSION) $(EPOCHS) 
