import streamlit as st 
import tensorflow as tf 
from utils import load_and_prep, get_classes


st.set_page_config(page_title="Food Vision", page_icon="🍔")
st.title("Food Vision 🍔📷")

model = tf.keras.models.load_model("./FoodVisionFineTunedModel.hdf5")

# @st.cache
def predicting(image, model):
    image = load_and_prep(image)
    image = tf.cast(tf.expand_dims(image, axis=0), tf.int16)
    preds = model.predict(image)
    pred_class = class_names[tf.argmax(preds[0])]
    pred_conf = tf.reduce_max(preds[0])
    return pred_class, pred_conf

class_names = get_classes()


file = st.file_uploader(label="Upload an image of food.",
                        type=["jpg", "jpeg", "png"])

if not file:
    st.warning("Please upload an image")
    st.stop()
else :
    image = file.read()
    st.image(image, use_column_width=True)
    pred_button = st.button("Predict")



if pred_button:
    pred_class, pred_conf = predicting(image, model)
    st.success(f'Prediction : {pred_class} \nConfidence : {pred_conf*100:.2f}%')
