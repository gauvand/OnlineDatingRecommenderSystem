# Online Dating Recommender System

## Project Description

The challenge of finding a romantic partner as well as the rise of the internet and social media in the 21st century has led to the immense popularity of online dating apps such as Tinder, Hinge, and Bumble. However, with over 270 million users of these services across the globe, there is the problem of information overload. In this paper, a social recommendation system to match users to candidate profiles is proposed to tackle this challenge. The use of user-oriented and item-oriented collaborative filtering is outlined as well as a reciprocal recommender system for use on the Libimseti online dating data set. Finally, evaluation metrics are defined for the comparisons between these models and a timeline for project progress is specified.

## Methods

For the purposes of this final project, I hope to build a collaborative filtering system or/and reciprocal recommendation system. My goal is to establish some form of comparison between the two models if time permits. If I am not able to develop a reciprocal recommendation system, the final project will be based off the collaborative filtering system outlined in this paper. I also aim to try and develop an item-oriented method to approaching this problem of predicting matches. Finally, I hope to use some form of ensemble model to combine the predictions from each of these models and use them in predicting the top candidate profile for a given user.

### User-oriented approach

In a user-user style collaborative filtering system, the algorithm first searches the database for users with similar ratings vectors to user $a$, who we wish to recommend candidates to. The $k$ most similar neighbours are then used to predict candidate $j$ based on the network of user $a$. I decided to use the approach taken by Brozovsky. According to this approach, the prediction for the user $a$ and profile $j$ is given by:
    
$
p_{a,j} = \overline{R_i} + \alpha \sum_{i = 1}^{k}w(a,n_i)(R_{n_i,j} - \overline{R_{n_i}}) 
$

Here, $\overline{R_{.,u}}$ refers to the mean rating given by user $u$, and $\alpha$ is the normalizing factor. The user-user similarity, $w$, can be calculated using a similarity metric such as the Pearson Correlation Coefficient. For two users $a$ and $j$:

$
w(a,j) = \frac{\sum_{i}(R_{ai} - \overline{R_{a}}) \cdot {R_{ji} - \overline{R_j}}}{\sqrt{  {\sum_{i}(R_{ai} - \overline{R_a})^2}}\sqrt{       \sum_{i}(R_{ji} - \overline{R_j})^2      }}
$


The summations from $i$ represent the indices of the top $k$ similar users to $a$ which have rated profile $j$. $n_i$ is the i-th most similar user to $a$. 

## Item-oriented approach

Similar to the user-user method, the item-oriented approach to collaborative filtering by Brozovsky uses the similarity between items or user profiles in an attempt to make a prediction for the active user $a$. The ratings of the top $k$ similar profiles from the user $a$ are then used to generate predictions for the profile $j$.

The prediction for the user $a$ and the profile $j$ is given by:

    
$
p_{a,j} = \overline{R_{.,j}} + \alpha \sum_{i = 1}^{k}{ \widetilde{ w}(j,n_i)(R_{a,n_i} - \overline{R_{.,n_i}}) }
$

Here, $\overline{R_{.,u}}$ refers to the mean rating of profile $u$, and $\alpha$ is the normalizing factor.

The item-item similarity, $\widetilde{w}$ can also be calculated using the Pearson Correlation Coefficient. For a profile $j$ and a profile $l$:


$
\widetilde{w}(j,l) = \frac{\sum_{i}(R_{ij} - \overline{R_{i}}) \cdot {R_{il} - \overline{R_i}}}{\sqrt{  {\sum_{i}(R_{ij} - \overline{R_i})^2}}\sqrt{       \sum_{i}(R_{il} - \overline{R_i})^2      }}
$

Here, the summations from $i$ represent the indices of the top $k$ similar profiles to $j$ which have been rated by user $a$. $n_i$ is the i-th most similar profile to $j$. 


## Reciprocal Recommendation approach

Several different ideas surrounding the implementation of reciprocal recommendation exist. \citet{pizzato10} suggest using their RECON implementation of the reciprocal recommender that takes into account several attributes that represent a user's interests (for example, personality type, body shape, education, etc.), and uses this information to gauge \textit{preference.} After obtaining the preferences, the recommender system is able to generate a list of people who match some of these attributes and assign them a \textit{compatibility score}. Finally, the reciprocal score, $R$, for users $x$ and $y$ can be calculated as:


$
R_{xy} = R_{yx} = \frac{2}{[\text{Compatibility}(P_x,y)]^{-1} + [\text{Compatibility}(P_y,x)]^{-1}}
$   


where $P_u$ represents the preferences of a user $u$ and $\text{Compatibility}(P_u,m)$ represents the compatibility score for user $m$ based on the preference of user $u$.


I aim to tackle this problem using a similar approach, if time permits.


