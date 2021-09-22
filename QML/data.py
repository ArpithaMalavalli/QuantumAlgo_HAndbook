import numpy as np

classMappings = {'red': 0, 'blue': 1}

trainingData = {
       'red': np.array(
              [[5.71769863, 1.31946891],
              [0.        , 2.45044227],
              [2.26194671, 0.69115038],
              [4.1469023 , 4.83805269],
              [0.62831853, 2.38761042],
              [4.46106157, 1.63362818],
              [1.19380521, 4.33539786],
              [2.95309709, 5.59203492],
              [2.136283  , 1.38230077],
              [3.83274304, 0.06283185],
              [6.22035345, 2.89026524],
              [5.71769863, 4.96371639],
              [2.82743339, 0.56548668],
              [1.94778745, 1.50796447],
              [4.0212386 , 3.20442451],
              [6.09468975, 5.96902604],
              [5.46637122, 0.56548668],
              [1.94778745, 1.44513262],
              [4.90088454, 1.44513262],
              [4.08407045, 1.57079633]]
       ), 'blue': np.array(
              [[3.0787608 , 1.31946891],
              [2.95309709, 4.58672527],
              [4.64955713, 5.52920307],
              [0.        , 1.82212374],
              [1.13097336, 1.88495559],
              [1.00530965, 4.96371639],
              [2.19911486, 1.94778745],
              [2.82743339, 1.69646003],
              [3.33008821, 3.70707933],
              [3.0787608 , 5.02654825],
              [0.62831853, 3.39292007],
              [5.2150438 , 3.64424748],
              [0.        , 1.88495559],
              [1.31946891, 5.84336234],
              [3.33008821, 3.70707933],
              [4.83805269, 2.19911486],
              [1.88495559, 2.89026524],
              [0.75398224, 3.26725636],
              [4.77522083, 4.1469023 ],
              [2.136283  , 5.2150438 ]]
       )
}

testData = {
       'red': np.array(
              [[4.52389342, 2.38761042],
              [2.89026524, 0.50265482],
              [0.18849556, 5.46637122],
              [1.50796447, 4.83805269],
              [0.81681409, 5.0893801 ],
              [4.52389342, 2.32477856],
              [0.62831853, 2.82743339],
              [4.58672527, 2.63893783],
              [0.        , 5.34070751],
              [4.46106157, 2.0106193 ]]
       ), 'blue': np.array(
              [[0.06283185, 1.19380521],
              [0.43982297, 4.90088454],
              [0.12566371, 1.82212374],
              [2.26194671, 5.2150438 ],
              [2.70176968, 0.31415927],
              [4.83805269, 5.96902604],
              [2.95309709, 1.82212374],
              [2.07345115, 3.70707933],
              [3.58141563, 1.57079633],
              [5.0893801 , 5.59203492]]
       )
}

predData = [np.array([[4.46106157, 3.14159265],
       [0.06283185, 2.32477856],
       [2.32477856, 4.33539786],
       [2.07345115, 1.44513262],
       [2.0106193 , 1.50796447],
       [2.38761042, 0.62831853],
       [2.57610598, 3.51858377],
       [5.78053048, 5.0893801 ],
       [2.82743339, 5.2150438 ],
       [4.58672527, 2.76460154],
       [2.07345115, 3.58141563],
       [3.0787608 , 4.0212386 ],
       [2.136283  , 0.50265482],
       [5.02654825, 5.15221195],
       [1.00530965, 2.51327412],
       [1.94778745, 3.58141563],
       [2.89026524, 3.95840674],
       [1.94778745, 2.63893783],
       [4.64955713, 0.18849556],
       [4.83805269, 0.43982297]]),
       np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])]
