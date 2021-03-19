# Online Dating Recommender System

## Project Description

The challenge of finding a romantic partner as well as the rise of the internet and social media in the 21st century has led to the immense popularity of online dating apps such as Tinder, Hinge, and Bumble. However, with over 270 million users of these services across the globe, there is the problem of information overload. In this paper, a social recommendation system to match users to candidate profiles is proposed to tackle this challenge. The use of user-oriented and item-oriented collaborative filtering is outlined as well as a reciprocal recommender system for use on the Libimseti online dating data set. Finally, evaluation metrics are defined for the comparisons between these models and a timeline for project progress is specified.

## Methods

For the purposes of this final project, I hope to build a collaborative filtering system or/and reciprocal recommendation system. My goal is to establish some form of comparison between the two models if time permits. If I am not able to develop a reciprocal recommendation system, the final project will be based off the collaborative filtering system outlined in this paper. I also aim to try and develop an item-oriented method to approaching this problem of predicting matches. Finally, I hope to use some form of ensemble model to combine the predictions from each of these models and use them in predicting the top candidate profile for a given user.

### User-oriented approach

In a user-user style collaborative filtering system, the algorithm first searches the database for users with similar ratings vectors to user  a , who we wish to recommend candidates to. The  k  most similar neighbours are then used to predict candidate  j  based on the network of user  a . I decided to use the approach taken by Brozovsky. According to this approach, the prediction for the user  a  and profile  j  is given by:
    
<img src = "https://latex.codecogs.com/png.latex?%5Cbg_white%20p_%7Ba%2Cj%7D%20%3D%20%5Coverline%7BR_i%7D%20&plus;%20%5Calpha%20%5Csum_%7Bi%20%3D%201%7D%5E%7Bk%7Dw%28a%2Cn_i%29%28R_%7Bn_i%2Cj%7D%20-%20%5Coverline%7BR_%7Bn_i%7D%7D%29" >

Here,  \overline{R_{.,u}}  refers to the mean rating given by user  u , and  \alpha  is the normalizing factor. The user-user similarity,  w , can be calculated using a similarity metric such as the Pearson Correlation Coefficient. For two users  a  and  j :

<img src = "https://latex.codecogs.com/png.latex?%5Cbg_white%20w%28a%2Cj%29%20%3D%20%5Cfrac%7B%5Csum_%7Bi%7D%28R_%7Bai%7D%20-%20%5Coverline%7BR_%7Ba%7D%7D%29%20%5Ccdot%20%7BR_%7Bji%7D%20-%20%5Coverline%7BR_j%7D%7D%7D%7B%5Csqrt%7B%20%7B%5Csum_%7Bi%7D%28R_%7Bai%7D%20-%20%5Coverline%7BR_a%7D%29%5E2%7D%7D%5Csqrt%7B%20%5Csum_%7Bi%7D%28R_%7Bji%7D%20-%20%5Coverline%7BR_j%7D%29%5E2%20%7D%7D">


The summations from  i  represent the indices of the top  k  similar users to  a  which have rated profile  j .  n_i  is the i-th most similar user to  a . 

### Item-oriented approach

Similar to the user-user method, the item-oriented approach to collaborative filtering by Brozovsky uses the similarity between items or user profiles in an attempt to make a prediction for the active user a. The ratings of the top  k  similar profiles from the user  a  are then used to generate predictions for the profile  j .

The prediction for the user  a  and the profile j is given by:

<img src = "https://latex.codecogs.com/png.latex?%5Cbg_white%20p_%7Ba%2Cj%7D%20%3D%20%5Coverline%7BR_%7B.%2Cj%7D%7D%20&plus;%20%5Calpha%20%5Csum_%7Bi%20%3D%201%7D%5E%7Bk%7D%7B%20%5Cwidetilde%7B%20w%7D%28j%2Cn_i%29%28R_%7Ba%2Cn_i%7D%20-%20%5Coverline%7BR_%7B.%2Cn_i%7D%7D%29%20%7D">
    
Here,  \overline{R_{.,u}}  refers to the mean rating of profile  u , and  \alpha  is the normalizing factor.

The item-item similarity,  \widetilde{w}  can also be calculated using the Pearson Correlation Coefficient. For a profile  j  and a profile  l :

<img src = "https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Cwidetilde%7Bw%7D%28j%2Cl%29%20%3D%20%5Cfrac%7B%5Csum_%7Bi%7D%28R_%7Bij%7D%20-%20%5Coverline%7BR_%7Bi%7D%7D%29%20%5Ccdot%20%7BR_%7Bil%7D%20-%20%5Coverline%7BR_i%7D%7D%7D%7B%5Csqrt%7B%20%7B%5Csum_%7Bi%7D%28R_%7Bij%7D%20-%20%5Coverline%7BR_i%7D%29%5E2%7D%7D%5Csqrt%7B%20%5Csum_%7Bi%7D%28R_%7Bil%7D%20-%20%5Coverline%7BR_i%7D%29%5E2%20%7D%7D">


Here, the summations from  i  represent the indices of the top  k  similar profiles to  j  which have been rated by user  a .  n_i  is the i-th most similar profile to  j . 


### Reciprocal Recommendation approach

Several different ideas surrounding the implementation of reciprocal recommendation exist. \Pizzato et al. suggest using their RECON implementation of the reciprocal recommender that takes into account several attributes that represent a user's interests (for example, personality type, body shape, education, etc.), and uses this information to gauge \textit{preference.} After obtaining the preferences, the recommender system is able to generate a list of people who match some of these attributes and assign them a \textit{compatibility score}. Finally, the reciprocal score,  R , for users  x  and  y  can be calculated as:


<img src = "https://latex.codecogs.com/png.latex?%5Cbg_white%20R_%7Bxy%7D%20%3D%20R_%7Byx%7D%20%3D%20%5Cfrac%7B2%7D%7B%5B%5Ctext%7BCompatibility%7D%28P_x%2Cy%29%5D%5E%7B-1%7D%20&plus;%20%5B%5Ctext%7BCompatibility%7D%28P_y%2Cx%29%5D%5E%7B-1%7D%7D">


where P_u represents the preferences of a user u and Compatibility(P_u,m) represents the compatibility score for user m based on the preference of user u.


I aim to tackle this problem using a similar approach, if time permits.

## Evaluation

To evaluate my recommender systems, the data set will be divided into two parts -- the training set  K  and the testing set  U . The recommenders will be trained on  K  and evaluated on  U . This is identical to the approach given by \citet{socrecreview}.To evaluate prediction accuracy on the ratings, we can measure the closeness of the predicted ratings to the true ratings by using the Mean Absolute Error (MAE), which is given by:

<img src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Ctext%7BMAE%7D%20%3D%20%5Cfrac%7B1%7D%7B%7CU%7C%7D%5Csum_%7B%28u_i%2Cv_j%29%20%5Cin%20U%7D%7B%7C%5Cmathbf%7BR%7D_%7Bij%7D%20-%20%5Chat%7B%5Cmathbf%7BR%7D%7D_%7Bij%7D%7C%7D">

This mean average can also be normalized by using a normalization constant   \alpha = \frac{1}{R_{max} - R_{min}}  to give the Normalized Mean Absolute Error (NMAE),

<img src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Ctext%7BNMAE%7D%20%3D%20%5Cfrac%7B%5Calpha%7D%7B%7CU%7C%7D%5Csum_%7B%28u_i%2Cv_j%29%20%5Cin%20U%7D%7B%7C%5Cmathbf%7BR%7D_%7Bij%7D%20-%20%5Chat%7B%5Cmathbf%7BR%7D%7D_%7Bij%7D%7C%7D">

To evaluate the reciprocity of matches, we will need to use a separate metric defined by \citet{pizzato10} as the \textit{Success Rate} of a list of recommendations  L  given to a user  x . The \textit{Success Rate} can be given by the proportion of ratings that are positive:

<img src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Ctext%7BSuccess%20Rate%7D%28x%2C%20L%29%20%3D%20%5Cfrac%7B%7C%5C%7Bpr%3A%5C%3B%20pr%20%5C%3B%20%5Cin%20%5C%3B%20L%2C%20%5C%3B%20pr%5Ctext%7B%20rated%20x%205%20or%20greater%7D%29%5C%7D%7C%7D%7B%7C%5C%7B%20kr%20%3A%20kr%20%5Cin%20L%2C%20kr%20%5Cin%20M_x%20%5C%7D%7C%7D">

where  M_u  is the set of all ratings that the user  u  has given.

We can also define a \textit{Recall Rate}, 
 
<img src= "https://latex.codecogs.com/png.latex?%5Cbg_white%20%5Ctext%7BRecall%20Rate%7D%28x%2C%20L%29%20%3D%20%5Cfrac%7B%7C%5C%7Bpr%3A%5C%3B%20pr%20%5C%3B%20%5Cin%20%5C%3B%20L%2C%20%5C%3B%20pr%5Ctext%7B%20rated%20x%205%20or%20greater%7D%29%5C%7D%7C%7D%7B%7C%5C%7B%20py%20%3A%20py%20%5C%3B%20%5Cin%20%5C%3B%20M_x%2C%20py%20%5Ctext%7B%20rated%20x%205%20or%20greater%7D%20%5C%7D%7C%7D">

These definitions are analogous to the common definitions of precision and recall. 

We can compare these metrics across all the models that we generate and identify which models perform better in each respect.



