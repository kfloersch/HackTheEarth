from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("model_ex-092_acc-0.959971.h5")
prediction.setJsonPath("model_class.json")
prediction.loadModel(num_objects=7)

predictions, probabilities = prediction.predictImage("948271.jpg", result_count=7)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)