#!/usr/bin/env python
# coding: utf-8

# ##Combining Factors
# Factors can be combined, both with other Factors and with scalar values, via any of the builtin mathematical operators (+, -, *, etc). This makes it easy to write complex expressions that combine multiple Factors. For example, constructing a Factor that computes the average of two other Factors is simply:
# ```
# >>> f1 = SomeFactor(...)
# >>> f2 = SomeOtherFactor(...)
# >>> average = (f1 + f2) / 2.0
# ```
# In this lesson, we will create a pipeline that creates a `relative_difference` factor by combining a 10-day average factor and a 30-day average factor. 
# 
# As usual, let's start with our imports:

# In[1]:


from quantopian.pipeline import Pipeline
from quantopian.research import run_pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import SimpleMovingAverage


# For this example, we need two factors: a 10-day mean close price factor, and a 30-day one:

# In[2]:


mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)


# Then, let's create a percent difference factor by combining our `mean_close_30` factor with our `mean_close_10` factor.

# In[3]:


percent_difference = (mean_close_10 - mean_close_30) / mean_close_30


# In this example, `percent_difference` is still a `Factor` even though it's composed as a combination of more primitive factors. We can add `percent_difference` as a column in our pipeline. Let's define `make_pipeline` to create a pipeline with `percent_difference` as a column (and not the mean close factors):

# In[4]:


def make_pipeline():

    mean_close_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
    mean_close_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)

    percent_difference = (mean_close_10 - mean_close_30) / mean_close_30

    return Pipeline(
        columns={
            'percent_difference': percent_difference
        }
    )


# Let's see what the new output looks like:

# In[6]:


result = run_pipeline(make_pipeline(), '2015-05-05', '2015-05-05')
result


# In the next lesson, we will learn about filters.
