import shap
import lime
import lime.lime_tabular
import matplotlib.pyplot as plt

def shap_explain(model, X):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    shap.summary_plot(shap_values, X)

def lime_explain(model, X_train, X_test, instance_index):
    explainer = lime.lime_tabular.LimeTabularExplainer(X_train.values, mode='classification', feature_names=X_train.columns)
    exp = explainer.explain_instance(X_test.iloc[instance_index].values, model.predict_proba)
    exp.show_in_notebook()
    exp.as_pyplot_figure()
    plt.show()
