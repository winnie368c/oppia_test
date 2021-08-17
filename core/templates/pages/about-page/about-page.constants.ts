// Copyright 2020 The Oppia Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * @fileoverview Constants for the Oppia about page.
 */

export const AboutPageConstants = {
  // These credits should not be changed directly. If any change is
  // made to structure/formatting, the respective constants
  // CREDITS_START_LINE, CREDITS_END_LINE and CREDITS_INDENT should be
  // updated in update_changelog_and_credits.py file. If the patterns do
  // not match, update_changelog_and_credits_test will fail.
  CREDITS_CONSTANTS: [
    'Aadya Mishra',
    'Aaron Zuspan',
    'Aashish Gaba',
    'Aashish Singh',
    'Aasif Faizal',
    'Abeer Khan',
    'Abhay Garg',
    'Abhay Gupta',
    'Abhay Raghuwanshi',
    'Abhay Raizada',
    'Abhijit Suresh',
    'Abhimanyu Thakre',
    'Abhishek Arya',
    'Abhishek Kumar',
    'Abhishek Uniyal',
    'Abhith Krishna',
    'Abraham Mgowano',
    'Acash Mkj',
    'Adarsh Kumar',
    'Aditya Dubey',
    'Aditya Jain',
    'Aditya Sharma',
    'Adrija Acharyya',
    'Aishwary Saxena',
    'Ajay Sharma',
    'Ajo John',
    'Akshath Kaushal',
    'Akshay Anand',
    'Akshay Nandwana',
    'Alex Gower',
    'Alex Lee',
    'Alexandra Wu',
    'Allan Zhou',
    'Alluri Harshit Varma',
    'Amanda Rodriguez',
    'Amey Kudari',
    'Amit Deutsch',
    'Amulya Kumar',
    'Ana Francisca Bernardo',
    'Andrew Low',
    'Andrey Mironyuk',
    'Angela Park',
    'Anggoro Dewanto',
    'Anish V Badri',
    'Ankita Saxena',
    'Anmol Mittal',
    'Anmol Shukla',
    'Anshul Hudda',
    'Anthony Alridge',
    'Anthony Zheng',
    'Anubhav Sinha',
    'Anumeha Agrawal',
    'Anurag Thakur',
    'Apurv Bajaj',
    'Apurv Botle',
    'Archi Aggarwal',
    'Areesha Tariq',
    'Arkadyuti Bandyopadhyay',
    'Arnesh Agrawal',
    'Arpan Banerjee',
    'Arpit Bandejiya',
    'Arun Kumar',
    'Arunabh Ghosh',
    'Aryaman Gupta',
    'Ashish Verma',
    'Ashmeet Singh',
    'Ashutosh Chauhan',
    'Ashutosh Singla',
    'Assem Yeskabyl',
    'Aubrey Wells',
    'Aung Hein Oo',
    'Austin Choi',
    'Avijit Gupta',
    'Ayush Kumar',
    'Ayush Nandi',
    'Baiba Skujevska',
    'Barnabas Makonda',
    'Ben Henning',
    'Ben Targan',
    'Benjamin Beeshma',
    'Bill Morrisson',
    'BJ Voth',
    'Bolaji Fatade',
    'Boyd Y. Ching',
    'Brenton Briggs',
    'Brian Lin',
    'Brian Rodriguez',
    'Cathleen Huang',
    'Charisse De Torres',
    'Chase Albert',
    'Chen Shenyue',
    'Chin Zhan Xiong',
    'Chris Skalnik',
    'Christopher Tao',
    'Cihan Bebek',
    'Connie Chow',
    'Corey Hunter',
    'Céline Deknop',
    'Darin Nguyen',
    'David Cheng',
    'Dawson Eliasen',
    'Debanshu Bhaumik',
    'Deepam Banerjee',
    'Deepank Agarwal',
    'Denis Samokhvalov',
    'Devi Sandeep',
    'Dharmesh Poddar',
    'Diana Chen',
    'Divyadeep Singh',
    'Domenico Vitarella',
    'Dong Wook Brian Chung',
    'Edward Allison',
    'Eesha Arif',
    'Elizabeth Kemp',
    'Emily Glue',
    'Eric Lou',
    'Eric Yang',
    'Estelle Lee',
    'Fang You',
    'Farees Hussain',
    'Felicity Zhao',
    'Florin Balint',
    'Frederik Creemers',
    'Gabriel Fuentes',
    'Gagan Suneja',
    'Gangavarapu Praneeth',
    'Gautam Verma',
    'Geet Choudhary',
    'Grace Guo',
    'Hadyn Fitzgerald',
    'Hamlet Villa',
    'Hamza Chandad',
    'Hanan Mufti',
    'Hardik Katehara',
    'Haresh Khanna',
    'Harsh Khajuria',
    'Harsh Khilawala',
    'Hasitha Kaushan',
    'Hema Sundara Rao Ginni',
    'Henriette Hettinga',
    'Henry Phu',
    'Himanshu Aggarwal',
    'Himanshu Dixit',
    'Hitesh Sharma',
    'Hitesh Tomar',
    'Hope Ngerebara',
    'Hossam Mohammed Alsheikh',
    'Huong Le',
    'Ian Luttrell',
    'Ishan Shanware',
    'Ishan Singh',
    'Jackson Wu',
    'Jacob Davis',
    'Jacob Li Peng Cheng',
    'Jacque Li',
    'Jakub Osika',
    'James James John',
    'James Xu',
    'Jamie Lau',
    'Jansen Yan',
    'Jared Silver',
    'Jasmine Rider',
    'Jasper Deng',
    'Jaswinder Singh',
    'Jayasanka Madhawa',
    'Jaysinh Shukla',
    'Jenna Mandel',
    'Jennifer Chen',
    'Jeremy Emerson',
    'Jerry Chen',
    'Jerry Lau',
    'Jian Fu',
    'Jiazhi Chen',
    'Jim Zhan',
    'John Glennon',
    'John Karasinski',
    'John Prince Mesape',
    'Jonathan Slaton',
    'Jordan Cockles',
    'Jordan Stapinski',
    'Joseph Fedota',
    'Joshua Cano',
    'Joshua Lan',
    'Joshua Lusk',
    'Joydeep Mukherjee',
    'Juan Saba',
    'Justin Du',
    'Jérôme',
    'K.N. Anantha Nandanan',
    'Kajol Kumari',
    'Karen Rustad',
    'Kartikey Pandey',
    'Kashif Jamal Soofi',
    'Kate Perkins',
    'Kathryn Patterson',
    'Kayla Hardie',
    'Kefeh Collins',
    'Kenneth Ho',
    'Kerry Wang',
    'Keshav Bathla',
    'Keshav Gupta',
    'Kevin Conner',
    'Kevin Lee',
    'Kevin Thomas',
    'Kevin Zhang',
    'Khushi Gangopadhyay',
    'Kiran Konduru',
    'Kishan Kumar',
    'Koji Ashida',
    'Konstantinos Kagkelidis',
    'Krishita Jain',
    'Krishna Rao',
    'Kristin Anthony',
    'Kumari Shalini',
    'Kunal Garg',
    'Kyriaki Velliniati',
    'Lakshay Angrish',
    'Lara Davies',
    'Laura Kinkead',
    'Linn Hallonqvist',
    'Lorrany Azevedo',
    'Lucklita Theng',
    'Luis Ulloa',
    'Lunrong Chen',
    'Madhav Sainanee',
    'Madiyar Aitbayev',
    'Mamat Rahmat',
    'Manas Tungare',
    'Manoj Mohan',
    'Marcel Schmittfull',
    'Mariana Zangrossi',
    'Mark Cabanero',
    'Mark Halpin',
    'Martin Smithurst',
    'Matt Higgins',
    'Maurício Meneghini Fauth',
    'Md Shahbaz Alam',
    'Meet Vyas',
    'Mert Degirmenci',
    'Michael Anuzis',
    'Michael Mossey',
    'Michael Orwin',
    'Michael Wagner',
    'Michael Wu',
    'Michelle R',
    'Milagro Teruel',
    'Min Tan',
    'Mohammad Shahebaz',
    'Mohammad Zaman',
    'Mohit Balwani',
    'Mohit Gupta',
    'Mohit Musaddi',
    'Mortaza Aghazadah',
    'Mozammel Haque',
    'Mridul Setia',
    'Mungo Dewar',
    'Nadin Tamer',
    'Nalin Bhardwaj',
    'Nalin Chhibber',
    'Naman Kalra',
    'Namuli Joyce',
    'Naveen Kumar Shukla',
    'Netaji Kancharapu',
    'Nicolas Skirkey',
    'Nikhil Agarwal',
    'Nikhil Handa',
    'Nikhil Nair',
    'Nikhil Prakash',
    'Nikhil Sangwan',
    'Nimalen Sivapalan',
    'Nisarg Chaudhari',
    'Nishant Mittal',
    'Nisheal John',
    'Nitanshu Lokhande',
    'Nithesh N. Hariharan',
    'Nitish Bansal',
    'Omshi Samal',
    'Oskar Cieslik',
    'Oswell Chan',
    'Owen Parry',
    'Ozan Filiz',
    'Paloma Oliveira',
    'Pankaj Dahiya',
    'Parth Bhoiwala',
    'Parul Priyedarshani',
    'Pawan Rai',
    'Pawel Borkar',
    'Phil Wagner',
    'Philip Hayes',
    'Phillip Moulton',
    'Piyush Agrawal',
    'Prakash Subedi',
    'Pranav Siddharth S',
    'Prasanna Patil',
    'Pratik Katte',
    'Prayush Dawda',
    'Pulkit Aggarwal',
    'Pulkit Gera',
    'Purhan',
    'Purvi Misal',
    'Radesh Kumar',
    'Rafay Ghafoor',
    'Rafał Kaszuba',
    'Rahul Gurung',
    'Rahul Modi',
    'Raine Hoover',
    'Rajan Garg',
    'Rajat Kumar',
    'Rajat Patwa',
    'Rajat Talesra',
    'Rajendra Kadam',
    'Rajitha Warusavitarana',
    'Rakshit Kumar',
    'Ramin Izadpanah',
    'Raymond Tso',
    'Rebekah Houser',
    'Reinaldo Aguiar',
    'Reshu Kumari',
    'Reto Brunner',
    'Ria Arora',
    'Richard Cho',
    'Rijuta Singh',
    'Rishabh Rawat',
    'Rishav Chakraborty',
    'Ritik Kumar',
    'Rizky Riyaldhi',
    'Robert Moreno Carrillo',
    'Rohan Batra',
    'Rohan Gulati',
    'Rohit Katlaa',
    'Ross Strader',
    'Rudra Sadhu',
    'Rémi Gourdon',
    'Sachin Chauhan',
    'Sachin Gopal',
    'Saeed Jassani',
    'Safwan Mansuri',
    'Sagang Wee',
    'Sagar Manohar',
    'Sajal Asati',
    'Sajen Sarvajith',
    'Sajna Kadalikat',
    'Samara Trilling',
    'Samriddhi Mishra',
    'Sandeep Dubey',
    'Sandeep Patel',
    'Sanjana Konte',
    'Sankranti Joshi',
    'Santos Hernandez',
    'Sanyam Khurana',
    'Sasa Cocic-Banjanac',
    'Satish Boggarapu',
    'Satmeet Ubhi',
    'Satwik Kansal',
    'Satyam Bhalla',
    'Satyam Yadav',
    'Saurav Pratihar',
    'Savitha K Jayasankar',
    'Scott Brenner',
    'Scott Junner',
    'Scott Roberts',
    'Sean Anthony Riordan',
    'Sean Lip',
    'Sebastian Zangaro',
    'Seth Beckman',
    'Seth Saloni',
    'Shafqat Dulal',
    'Shantanu Bhowmik',
    'Sharif Shaker',
    'Shiqi Wu',
    'Shitong Shou',
    'Shiva Krishna Yadav',
    'Shivan Trivedi',
    'Shivansh Bajaj',
    'Shivansh Dhiman',
    'Shivansh Rakesh',
    'Shouvik Roy',
    'Shruti Grover',
    'Shruti Satish',
    'Shubha Gupta',
    'Shubha Rajan',
    'Shubham Bansal',
    'Shubham Korde',
    'Shuta Suzuki',
    'Siddhant Khandelwal',
    'Siddhant Srivastav',
    'Siddharth Batra',
    'Simran Mahindrakar',
    'Souhit Dey',
    'Soumyo Dey',
    'Sourab Jha',
    'Sourav Badami',
    'Sourav Singh',
    'Sreenivasulu Giritheja',
    'Srijan Reddy',
    'Srikanth Kadaba',
    'Srikar Ch',
    'Stefanie Muroya Lei',
    'Stephanie Federwisch',
    'Stephen Chiang',
    'Stephen Hannon',
    'Steve Jiang',
    'Subodh Verma',
    'Sudhanva MG',
    'Sudipta Gyan Prakash Pradhan',
    'Sumit Paroothi',
    'Surya Siriki',
    'Taiwo Adetona',
    'Tanishq Gupta',
    'Tanmay Mathur',
    'Tarashish Mishra',
    'Teddy Marchildon',
    'Tezuesh Varshney',
    'Theo Lipeles',
    'Tia Jin',
    'Tianqi Wu',
    'Timothy Cyrus',
    'Tonatiuh Garcia',
    'Tony Afula',
    'Tony Jiang',
    'Tracy Homer',
    'Travis Shafer',
    'Truong Kim',
    'Tuguldur Baigalmaa',
    'Tushar Mohan',
    'Tyler Ishikawa',
    'Ujjwal Gulecha',
    'Umesh Singla',
    'Utkarsh Dixit',
    'Varazdat Manukyan',
    'Varun Tandon',
    'Vasu Tomar',
    'Vibhor Agarwal',
    'Viet Tran Quoc Hoang',
    'Vijay Patel',
    'Viktor Pishuk',
    'Vinayak Vishwanath Gosain',
    'Vinit Dantkale',
    'Vinita Murthi',
    'Viraj Prabhu',
    'Vishal Desai',
    'Vishal Gupta',
    'Vuyisile Ndlovu',
    'Y. Budhachandra Singh',
    'Yash Santosh Kandalkar',
    'Vishal Joisar',
    'Vishnu M',
    'Vojtěch Jelínek',
    'Vuyisile Ndlovu',
    'Wiktor Idzikowski',
    'Will Li',
    'Wilson Hong',
    'Xinyu Wu',
    'Xuân (Sean) Lương',
    'Yana Malysheva',
    'Yang Lu',
    'Yash Jipkate',
    'Yash Ladha',
    'Yi Yan',
    'Yiming Pan',
    'Yogesh Sharma',
    'Yousef Hamza',
    'Yuan Gu',
    'Yuliang',
    'Zach Puller',
    'Zach Wiebesiek',
    'Zachery Vekovius',
    'Zhu Chu',
    'Zoe Madden-Wood',
  ]
} as const;
