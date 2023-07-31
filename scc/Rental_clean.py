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
    "import seaborn as sns"
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
       "      <th>rental_id</th>\n",
       "      <th>rental_date</th>\n",
       "      <th>inventory_id</th>\n",
       "      <th>customer_id</th>\n",
       "      <th>return_date</th>\n",
       "      <th>staff_id</th>\n",
       "      <th>last_update</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2005-05-24 22:53:30</td>\n",
       "      <td>367</td>\n",
       "      <td>130</td>\n",
       "      <td>2005-05-26 22:04:30</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 21:30:53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2005-05-24 22:54:33</td>\n",
       "      <td>1525</td>\n",
       "      <td>459</td>\n",
       "      <td>2005-05-28 19:40:33</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 21:30:53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2005-05-24 23:03:39</td>\n",
       "      <td>1711</td>\n",
       "      <td>408</td>\n",
       "      <td>2005-06-01 22:12:39</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 21:30:53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2005-05-24 23:04:41</td>\n",
       "      <td>2452</td>\n",
       "      <td>333</td>\n",
       "      <td>2005-06-03 01:43:41</td>\n",
       "      <td>2</td>\n",
       "      <td>2006-02-15 21:30:53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2005-05-24 23:05:21</td>\n",
       "      <td>2079</td>\n",
       "      <td>222</td>\n",
       "      <td>2005-06-02 04:33:21</td>\n",
       "      <td>1</td>\n",
       "      <td>2006-02-15 21:30:53</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   rental_id          rental_date  inventory_id  customer_id  \\\n",
       "0          1  2005-05-24 22:53:30           367          130   \n",
       "1          2  2005-05-24 22:54:33          1525          459   \n",
       "2          3  2005-05-24 23:03:39          1711          408   \n",
       "3          4  2005-05-24 23:04:41          2452          333   \n",
       "4          5  2005-05-24 23:05:21          2079          222   \n",
       "\n",
       "           return_date  staff_id          last_update  \n",
       "0  2005-05-26 22:04:30         1  2006-02-15 21:30:53  \n",
       "1  2005-05-28 19:40:33         1  2006-02-15 21:30:53  \n",
       "2  2005-06-01 22:12:39         1  2006-02-15 21:30:53  \n",
       "3  2005-06-03 01:43:41         2  2006-02-15 21:30:53  \n",
       "4  2005-06-02 04:33:21         1  2006-02-15 21:30:53  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rentals = '../data/rental.csv'\n",
    "rental = pd.read_csv(rentals)\n",
    "pd.set_option('display.max_columns', None)\n",
    "\n",
    "rental.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "06ce3cef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rental_id       1000\n",
      "rental_date      999\n",
      "inventory_id    1000\n",
      "customer_id      485\n",
      "return_date      997\n",
      "staff_id           2\n",
      "last_update        1\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "unique_rental = rental.nunique()\n",
    "print(unique_rental)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dc9962a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000 entries, 0 to 999\n",
      "Data columns (total 7 columns):\n",
      " #   Column        Non-Null Count  Dtype \n",
      "---  ------        --------------  ----- \n",
      " 0   rental_id     1000 non-null   int64 \n",
      " 1   rental_date   1000 non-null   object\n",
      " 2   inventory_id  1000 non-null   int64 \n",
      " 3   customer_id   1000 non-null   int64 \n",
      " 4   return_date   1000 non-null   object\n",
      " 5   staff_id      1000 non-null   int64 \n",
      " 6   last_update   1000 non-null   object\n",
      "dtypes: int64(4), object(3)\n",
      "memory usage: 254.0 KB\n"
     ]
    }
   ],
   "source": [
    "rental.info(memory_usage='deep')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4aac0619",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "duplicate_rental = rental.duplicated().sum()\n",
    "print(duplicate_rental)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e561e25b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['rental_id', 'rental_date', 'inventory_id', 'customer_id', 'return_date', 'staff_id', 'last_update']\n"
     ]
    }
   ],
   "source": [
    "column_rental_list = rental.columns.tolist()\n",
    "print(column_rental_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "de8302a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['rental_id', 'return_date', 'rental_date', 'inventory_id', 'customer_id', 'staff_id', 'last_update']\n"
     ]
    }
   ],
   "source": [
    "_columns = ['rental_id', 'return_date', 'rental_date', 'inventory_id', 'customer_id', 'staff_id', 'last_update']\n",
    "\n",
    "rental = rental[_columns]\n",
    "column_rental_list = rental.columns.tolist()\n",
    "print(column_rental_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2e4b4571",
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
       "      <th>rental_id</th>\n",
       "      <th>return_date</th>\n",
       "      <th>rental_date</th>\n",
       "      <th>inventory_id</th>\n",
       "      <th>customer_id</th>\n",
       "      <th>staff_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2005-05-26 22:04:30</td>\n",
       "      <td>2005-05-24 22:53:30</td>\n",
       "      <td>367</td>\n",
       "      <td>130</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2005-05-28 19:40:33</td>\n",
       "      <td>2005-05-24 22:54:33</td>\n",
       "      <td>1525</td>\n",
       "      <td>459</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2005-06-01 22:12:39</td>\n",
       "      <td>2005-05-24 23:03:39</td>\n",
       "      <td>1711</td>\n",
       "      <td>408</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2005-06-03 01:43:41</td>\n",
       "      <td>2005-05-24 23:04:41</td>\n",
       "      <td>2452</td>\n",
       "      <td>333</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2005-06-02 04:33:21</td>\n",
       "      <td>2005-05-24 23:05:21</td>\n",
       "      <td>2079</td>\n",
       "      <td>222</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   rental_id          return_date          rental_date  inventory_id  \\\n",
       "0          1  2005-05-26 22:04:30  2005-05-24 22:53:30           367   \n",
       "1          2  2005-05-28 19:40:33  2005-05-24 22:54:33          1525   \n",
       "2          3  2005-06-01 22:12:39  2005-05-24 23:03:39          1711   \n",
       "3          4  2005-06-03 01:43:41  2005-05-24 23:04:41          2452   \n",
       "4          5  2005-06-02 04:33:21  2005-05-24 23:05:21          2079   \n",
       "\n",
       "   customer_id  staff_id  \n",
       "0          130         1  \n",
       "1          459         1  \n",
       "2          408         1  \n",
       "3          333         2  \n",
       "4          222         1  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rental = rental.drop('last_update', axis=1)\n",
    "rental.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5ed30bbf",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "rental.to_csv('rental_clean.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a592bffc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af430f8b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73706bb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e80bde0a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e299a27b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af852584",
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
