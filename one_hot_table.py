lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data['human'] = (data['whoAmI'] == 'human').astype(int)
data['robot'] = (data['whoAmI'] == 'robot').astype(int)

data.head()
