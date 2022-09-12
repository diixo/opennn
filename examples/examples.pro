#   OpenNN: Open Neural Networks Library
#   www.opennn.net                                                                                
#                                                                                                 
#   O P E N N N   E X A M P L E S                                                                 
#                                                                                                 
#   Artificial Intelligence Techniques SL (Artelnics)                                             
#   artelnics@artelnics.com                                                                       

TEMPLATE = subdirs

CONFIG += ordered

SUBDIRS += airfoil_self_noise
SUBDIRS += airline_passengers
SUBDIRS += amazon_reviews
SUBDIRS += breast_cancer
SUBDIRS += iris_plant
SUBDIRS += logical_operations
SUBDIRS += mnist
SUBDIRS += object_detector
SUBDIRS += outlier_detection
SUBDIRS += rosenbrock
SUBDIRS += simple_approximation
SUBDIRS += simple_classification

win32:!win32-g++{
#QMAKE_CXXFLAGS+= -arch:AVX
#QMAKE_CFLAGS+= -arch:AVX
}

# OpenMP library

win32:!win32-g++{
QMAKE_CXXFLAGS += -std=c++17 -fopenmp -pthread #-lgomp -openmp
QMAKE_LFLAGS += -fopenmp -pthread #-lgomp -openmp
LIBS += -fopenmp -pthread #-lgomp
}else:!macx{QMAKE_CXXFLAGS+= -fopenmp -lgomp -std=c++17
QMAKE_LFLAGS += -fopenmp -lgomp
LIBS += -fopenmp -pthread -lgomp
}else: macx{
INCLUDEPATH += /usr/local/opt/libomp/include
LIBS += /usr/local/opt/libomp/lib/libomp.dylib}
