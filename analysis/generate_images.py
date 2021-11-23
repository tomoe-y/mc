from TreeImageGenerator import TreeImageGenerator
import tqdm
import sys

def main():
    target_file = sys.argv[1]
    #tree = TreeImageGenerator("/home/tomoe/mc/bench/test0.root")
    tree = TreeImageGenerator(target_file)
    tree.search_spesific_event()

    for i in tqdm.tqdm(tree.drawable_event_indexs):
        tree.get_entry(i)
        tree.draw_track(is_save_gif=True)

if __name__ == '__main__':
    main()