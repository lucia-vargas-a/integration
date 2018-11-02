import sys
import csv
 def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
     for line in reader:
        try:
            if(len(line)) == 19:
                id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
                source = "Node"
                writer.writerow([author_id, source, int(id), title, tagnames, node_type, parent_id, abs_parent_id, added_at, score])
            else:
                user_ptr_id, reputation, gold, silver, bronze = line
                source = "User"
                writer.writerow([int(user_ptr_id), source, reputation, gold, silver, bronze])
        except ValueError:
            continue
 if __name__ == "__main__":
    mapper()
