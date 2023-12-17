Our model surpasses the performance of the model presented in the DeepFood Paper, both trained on the same dataset. We employed mixed precision training and EfficientNetB0, optimizing the training process by implementing efficient data pipelines using tf.data API methods like batch() and prefetch().

DeepFood achieved an accuracy of 77.4%, whereas our model achieved an even higher accuracy of 80%. Notably, the training time for DeepFood's model spanned 2-3 days, while our model was trained in a remarkably shorter duration—just 30 minutes.

<img width="960" alt="food-1" src="https://github.com/aayushxrj/Food-Vision/assets/111623667/87ac5423-3a31-4fca-a792-ba44bdc5277c">


<img width="960" alt="food-4" src="https://github.com/aayushxrj/Food-Vision/assets/111623667/b103e5bc-9941-410c-a33c-63491e5c119e">



<img width="960" alt="food-5" src="https://github.com/aayushxrj/Food-Vision/assets/111623667/5f429f1f-3481-4f01-91f5-1b42b4aff9c7">
