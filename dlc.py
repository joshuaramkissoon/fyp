import deeplabcut
import os
from os import listdir

def setupProject(projectName, videos):
    return deeplabcut.create_new_project(projectName, 'joshua', videos) 
    
def extract_frames(path_config, mode):
    deeplabcut.extract_frames(path_config, mode)

def label_frames(path_config):
    deeplabcut.label_frames(path_config)

def getVideos(view, path, filetype):
    ### Returns all videos in folder and subfolders
    ### View can be 'side' or 'top'

    videos = []
    # currVids = getVideoNames('all', os.path.expanduser('~/Documents/fyp_videos/AllVideos-joshua-2020-05-23/videos'), '.mov')
    currVids = []
    for p, subdirs, files in os.walk(path):
        for name in files:
            if 'scattered' not in name and 'test' not in name:
                if filetype in name and view == 'all' and name not in currVids:
                    videos.append(os.path.join(p, name))
                elif filetype in name and view in name and name not in currVids:
                        videos.append(os.path.join(p, name))
    return videos


def getVideoNames(view, path, filetype):
    ### Returns names of videos in folder
    videos = []
    for p, subdirs, files in os.walk(path):
        for name in files:
            if filetype in name and view == 'all':
                videos.append(name)
            if filetype in name and view in name:
                videos.append(name)
    return videos

def getVideosNotPresent(allVideos, currentVideos):
    return [vid for vid in allVideos if vid not in currentVideos]

def getPathForPreprocessed(trials):
    paths = ['~/Documents/fyp_videos/Preprocessed/Trial ' + str(trial) + '/' for trial in trials]
    return [os.path.expanduser(path) for path in paths]

if __name__ == '__main__':
    # setup = True
    setup = False
    video_path = os.path.expanduser('~/Documents/fyp_videos/Preprocessed/')
    videos = []
    view = 'all'
    paths = getPathForPreprocessed(trials=[3,4,5,6,7])
    for path in paths:
        videos += getVideos(view, path, '.mov')
    projectName = 'orientation-invariant'
    if setup:
        path = setupProject(projectName, videos)
        print(path)
    else:
        path = '/Users/joshuaramkissoon/Documents/fyp_videos/AllVideos-joshua-2020-05-23/config.yaml'
        # deeplabcut.add_new_videos(path,videos)
        # extract_frames(path, 'automatic')
        label_frames(path)
        # allTrainShuffle1, shuffle1test = deeplabcut.mergeandsplit(path, trainindex=6, uniform=False)
        # print('Shuffle 1')
        # print('All train: ', allTrainShuffle1)
        # # print('Filtered train: ', shuffletrain)
        # print('Test: ', shuffle1test)






