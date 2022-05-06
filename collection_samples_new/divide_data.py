from lxml import etree
import argparse
import random
import spacy
import glob
import re
import os
import sys


def get_all_data(data_path):
    collection = etree.parse(data_path)
    all_entities = collection.xpath('//entity')
    return all_entities

def extract_save_entities(train_sample_entities, dev_sample_entites, output_train_path, output_dev_path):
    sample_doc = etree.Element('data', id='train')
    sample_entities_xml = etree.SubElement(sample_doc, 'entities')
    for entity in train_sample_entities:
        sample_entities_xml.append(entity)
    sample_tree = etree.ElementTree(sample_doc)
    with open(output_train_path, 'wb') as sample_file:
        sample_tree.write(sample_file, xml_declaration=True, encoding='utf-8')




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', default='train.xml', type=str,
                        help='path of data collections')
    parser.add_argument('--dev_sample_size', default=1000, type=int,
                        help='number of sample datas')
    parser.add_argument('--output_train_path', default='train_samples.xml', type=str,
                        help='path of train data samples')
    parser.add_argument('--output_dev_path', default='dev_samples.xml', type=str,
                        help='path of dev data samples')
    args = parser.parse_args()

    all_entities = get_all_data(args.data_path)
    random.shuffle(all_entities)
    train_sample_entities = all_entities[0:-args.dev_sample_size]
    dev_sample_entites = all_entities[-args.dev_sample_size:]
    extract_save_entities(train_sample_entities, dev_sample_entites, args.output_train_path, args.output_dev_path)