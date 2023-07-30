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
       "      <th>category_id</th>\n",
       "      <th>name</th>\n",
       "      <th>last_update</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Action</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Animation</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Children</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Classics</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Comedy</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   category_id       name          last_update\n",
       "0            1     Action  2006-02-15 04:46:27\n",
       "1            2  Animation  2006-02-15 04:46:27\n",
       "2            3   Children  2006-02-15 04:46:27\n",
       "3            4   Classics  2006-02-15 04:46:27\n",
       "4            5     Comedy  2006-02-15 04:46:27"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "categories = '../data/category.csv'\n",
    "category = pd.read_csv(categories)\n",
    "pd.set_option('display.max_columns', None)\n",
    "\n",
    "\n",
    "\n",
    "category.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5ed30bbf",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "category_id    16\n",
      "name           16\n",
      "last_update     1\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "unique_category = category.nunique()\n",
    "print(unique_category)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "93f415d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unique values of column 'category_id':\n",
      "[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]\n",
      "\n",
      "Unique values of column 'name':\n",
      "['Action' 'Animation' 'Children' 'Classics' 'Comedy' 'Documentary' 'Drama'\n",
      " 'Family' 'Foreign' 'Games' 'Horror' 'Music' 'New' 'Sci-Fi' 'Sports'\n",
      " 'Travel']\n",
      "\n",
      "Unique values of column 'last_update':\n",
      "['2006-02-15 04:46:27']\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for column in category.columns:\n",
    "    unique_values = category[column].unique()\n",
    "    print(f\"Unique values of column '{column}':\")\n",
    "    print(unique_values)\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
      "RangeIndex: 16 entries, 0 to 15\n",
      "Data columns (total 3 columns):\n",
      " #   Column       Non-Null Count  Dtype \n",
      "---  ------       --------------  ----- \n",
      " 0   category_id  16 non-null     int64 \n",
      " 1   name         16 non-null     object\n",
      " 2   last_update  16 non-null     object\n",
      "dtypes: int64(1), object(2)\n",
      "memory usage: 2.4 KB\n"
     ]
    }
   ],
   "source": [
    "category.info(memory_usage='deep')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "af430f8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(16, 3)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5695d7e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "category.set_index('category_id', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
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
       "      <th>name</th>\n",
       "      <th>last_update</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>category_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Action</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Animation</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Children</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Classics</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Comedy</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  name          last_update\n",
       "category_id                                \n",
       "1               Action  2006-02-15 04:46:27\n",
       "2            Animation  2006-02-15 04:46:27\n",
       "3             Children  2006-02-15 04:46:27\n",
       "4             Classics  2006-02-15 04:46:27\n",
       "5               Comedy  2006-02-15 04:46:27"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fe4bd692",
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
    "duplicate_category = category.duplicated().sum()\n",
    "print(duplicate_category)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "af852584",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "category_id\n",
      "1     False\n",
      "2     False\n",
      "3     False\n",
      "4     False\n",
      "5     False\n",
      "6     False\n",
      "7     False\n",
      "8     False\n",
      "9     False\n",
      "10    False\n",
      "11    False\n",
      "12    False\n",
      "13    False\n",
      "14    False\n",
      "15    False\n",
      "16    False\n",
      "dtype: bool\n"
     ]
    }
   ],
   "source": [
    "rows_with_null = category.isnull().all(axis=1)\n",
    "\n",
    "print(rows_with_null)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2157c77d",
   "metadata": {},
   "outputs": [],
   "source": [
    "category = category.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cbb05ae3",
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
       "      <th>index</th>\n",
       "      <th>category_id</th>\n",
       "      <th>name</th>\n",
       "      <th>last_update</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Action</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Animation</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>Children</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>Classics</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>Comedy</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index  category_id       name          last_update\n",
       "0      0            1     Action  2006-02-15 04:46:27\n",
       "1      1            2  Animation  2006-02-15 04:46:27\n",
       "2      2            3   Children  2006-02-15 04:46:27\n",
       "3      3            4   Classics  2006-02-15 04:46:27\n",
       "4      4            5     Comedy  2006-02-15 04:46:27"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "3c2a0966",
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
       "      <th>category_id</th>\n",
       "      <th>name</th>\n",
       "      <th>last_update</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Action</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Animation</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Children</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Classics</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Comedy</td>\n",
       "      <td>2006-02-15 04:46:27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   category_id       name          last_update\n",
       "0            1     Action  2006-02-15 04:46:27\n",
       "1            2  Animation  2006-02-15 04:46:27\n",
       "2            3   Children  2006-02-15 04:46:27\n",
       "3            4   Classics  2006-02-15 04:46:27\n",
       "4            5     Comedy  2006-02-15 04:46:27"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category = category.drop('index', axis=1)\n",
    "category.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbcb55fc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bd8bdcd8",
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
       "      <th>category_id</th>\n",
       "      <th>name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Action</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Animation</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Children</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Classics</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Comedy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   category_id       name\n",
       "0            1     Action\n",
       "1            2  Animation\n",
       "2            3   Children\n",
       "3            4   Classics\n",
       "4            5     Comedy"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category = category.drop('last_update', axis=1)\n",
    "category.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f30eb57b",
   "metadata": {},
   "outputs": [],
   "source": [
    "category.to_csv('category_clean.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ed59dc2",
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
