{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8f792c3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "90dd81d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>inventory_id</th>\n",
       "      <th>film_id</th>\n",
       "      <th>store_id</th>\n",
       "      <th>last_update</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   inventory_id  film_id  store_id          last_update\n",
       "0             1        1         1  2006-02-15 05:09:17\n",
       "1             2        1         1  2006-02-15 05:09:17\n",
       "2             3        1         1  2006-02-15 05:09:17\n",
       "3             4        1         1  2006-02-15 05:09:17\n",
       "4             5        1         2  2006-02-15 05:09:17\n",
       "5             6        1         2  2006-02-15 05:09:17\n",
       "6             7        1         2  2006-02-15 05:09:17\n",
       "7             8        1         2  2006-02-15 05:09:17\n",
       "8             9        2         2  2006-02-15 05:09:17\n",
       "9            10        2         2  2006-02-15 05:09:17"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventories = '../data/inventory.csv'\n",
    "inventory = pd.read_csv(inventories)\n",
    "pd.set_option('display.max_columns', None)\n",
    "\n",
    "inventory.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c0a380da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1      8\n",
       "127    8\n",
       "73     8\n",
       "174    8\n",
       "86     8\n",
       "      ..\n",
       "62     2\n",
       "53     2\n",
       "52     2\n",
       "196    2\n",
       "223    2\n",
       "Name: film_id, Length: 207, dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory.film_id.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "652cae92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1000, 4)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5ed30bbf",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inventory_id    1000\n",
      "film_id          207\n",
      "store_id           2\n",
      "last_update        1\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "unique_inventory = inventory.nunique()\n",
    "print(unique_inventory)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cd218e7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a592bffc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000 entries, 0 to 999\n",
      "Data columns (total 4 columns):\n",
      " #   Column        Non-Null Count  Dtype \n",
      "---  ------        --------------  ----- \n",
      " 0   inventory_id  1000 non-null   int64 \n",
      " 1   film_id       1000 non-null   int64 \n",
      " 2   store_id      1000 non-null   int64 \n",
      " 3   last_update   1000 non-null   object\n",
      "dtypes: int64(3), object(1)\n",
      "memory usage: 97.8 KB\n"
     ]
    }
   ],
   "source": [
    "inventory.info(memory_usage='deep')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "af430f8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1000, 4)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5695d7e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory.set_index('inventory_id', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "335534a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>film_id</th>\n",
       "      <th>store_id</th>\n",
       "      <th>last_update</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>inventory_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2006-02-15 05:09:17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              film_id  store_id          last_update\n",
       "inventory_id                                        \n",
       "1                   1         1  2006-02-15 05:09:17\n",
       "2                   1         1  2006-02-15 05:09:17\n",
       "3                   1         1  2006-02-15 05:09:17\n",
       "4                   1         1  2006-02-15 05:09:17\n",
       "5                   1         2  2006-02-15 05:09:17"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3afc2c72",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>film_id</th>\n",
       "      <th>store_id</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>inventory_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              film_id  store_id\n",
       "inventory_id                   \n",
       "1                   1         1\n",
       "2                   1         1\n",
       "3                   1         1\n",
       "4                   1         1\n",
       "5                   1         2"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory.drop([\"last_update\"], axis=1, inplace=True)\n",
    "inventory.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "967c9e15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inventory_id\n",
      "1       False\n",
      "2       False\n",
      "3       False\n",
      "4       False\n",
      "5       False\n",
      "        ...  \n",
      "996     False\n",
      "997     False\n",
      "998     False\n",
      "999     False\n",
      "1000    False\n",
      "Length: 1000, dtype: bool\n"
     ]
    }
   ],
   "source": [
    "rows_with_null = inventory.isnull().all(axis=1)\n",
    "\n",
    "print(rows_with_null)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "52d9da1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory.to_csv('filename.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2bee64e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>inventory_id</th>\n",
       "      <th>film_id</th>\n",
       "      <th>store_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   inventory_id  film_id  store_id\n",
       "0             1        1         1\n",
       "1             2        1         1\n",
       "2             3        1         1\n",
       "3             4        1         1\n",
       "4             5        1         2"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inventory = inventory.reset_index()\n",
    "inventory.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e0d15110",
   "metadata": {},
   "outputs": [],
   "source": [
    "inventory.to_csv('inventory_clean.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7fc3ca9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
