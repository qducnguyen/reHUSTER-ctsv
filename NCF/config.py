# dataset name 
# model name 
model = 'NeuMF-end'
assert model in ['MLP', 'GMF', 'NeuMF-end', 'NeuMF-pre']

# paths
main_path = './data/'

train_rating = main_path + 'df_train_map.pkl'
test_rating = main_path + 'df_test_map.pkl'
test_negative = main_path + 'negative_test_rating_map.pkl'

model_path = './models/'
GMF_model_path = model_path + 'GMF.pth'
MLP_model_path = model_path + 'MLP.pth'
NeuMF_model_path = model_path + 'NeuMF.pth'
