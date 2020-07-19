
import pandas as pd
import numpy as np

group = ['x','y','z']
data = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)],
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(12,50,10)
})

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
data.groupby('group').agg({'age':"count"})
data.groupby('group')['age'].nunique()

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
# df.cum()