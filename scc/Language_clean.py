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
       "      <th>language_id</th>\n",
       "      <th>name</th>\n",
       "      <th>last_update</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>English</td>\n",
       "      <td>2006-02-15 05:02:19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Italian</td>\n",
       "      <td>2006-02-15 05:02:19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Japanese</td>\n",
       "      <td>2006-02-15 05:02:19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Mandarin</td>\n",
       "      <td>2006-02-15 05:02:19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>French</td>\n",
       "      <td>2006-02-15 05:02:19</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   language_id      name          last_update\n",
       "0            1   English  2006-02-15 05:02:19\n",
       "1            2   Italian  2006-02-15 05:02:19\n",
       "2            3  Japanese  2006-02-15 05:02:19\n",
       "3            4  Mandarin  2006-02-15 05:02:19\n",
       "4            5    French  2006-02-15 05:02:19"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "languages = '../data/language.csv'\n",
    "language = pd.read_csv(languages)\n",
    "pd.set_option('display.max_columns', None)\n",
    "\n",
    "\n",
    "\n",
    "language.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "652cae92",
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
       "      <th>language_id</th>\n",
       "      <th>audio_type</th>\n",
       "      <th>audio_language</th>\n",
       "      <th>subtitle_Y/N</th>\n",
       "      <th>subtitle_language</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Orig</td>\n",
       "      <td>English</td>\n",
       "      <td>Y</td>\n",
       "      <td>Spanish</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Orig</td>\n",
       "      <td>English</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Dub</td>\n",
       "      <td>Spanish</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   language_id audio_type audio_language subtitle_Y/N subtitle_language\n",
       "0            1       Orig        English            Y           Spanish\n",
       "1            2       Orig        English            N                 N\n",
       "2            3        Dub        Spanish            N                 N"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_languages = {\n",
    "    'language_id': [1, 2, 3],\n",
    "    'audio_type': ['Orig', 'Orig', 'Dub'],\n",
    "    'audio_language': ['English', 'English', 'Spanish'],\n",
    "    'subtitle_Y/N': ['Y', 'N', 'N'],\n",
    "    'subtitle_language': ['Spanish', 'N', 'N']\n",
    "}\n",
    "\n",
    "new_language = pd.DataFrame(new_languages)\n",
    "new_language.head()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5ed30bbf",
   "metadata": {
    "scrolled": true
   },
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
       "      <th>language_id</th>\n",
       "      <th>audio_type</th>\n",
       "      <th>audio_language</th>\n",
       "      <th>subtitle_Y/N</th>\n",
       "      <th>subtitle_language</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Orig</td>\n",
       "      <td>English</td>\n",
       "      <td>Y</td>\n",
       "      <td>Spanish</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Orig</td>\n",
       "      <td>English</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Dub</td>\n",
       "      <td>Spanish</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   language_id audio_type audio_language subtitle_Y/N subtitle_language\n",
       "0            1       Orig        English            Y           Spanish\n",
       "1            2       Orig        English            N                 N\n",
       "2            3        Dub        Spanish            N                 N"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "language = new_language\n",
    "language.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3cd218e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    False\n",
      "1    False\n",
      "2    False\n",
      "dtype: bool\n"
     ]
    }
   ],
   "source": [
    "rows_with_null = language.isnull().all(axis=1)\n",
    "\n",
    "print(rows_with_null)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fce26987",
   "metadata": {},
   "outputs": [],
   "source": [
    "language.to_csv('language_clean.csv', index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67e400f1",
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
